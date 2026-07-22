from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta, timezone, date

from ..database import get_db
from ..models import DiagnosisResult, UserAnswer, Question, Unit, Category, Layer, User

router = APIRouter(prefix="/history", tags=["history"])

JST = timezone(timedelta(hours=9))
DAILY_GOAL = 10
XP_PER_LEVEL = 300


def _to_jst_date(dt: datetime) -> date:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(JST).date()


@router.get("/{user_id}/motivation")
def get_motivation(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    answers = db.query(UserAnswer).filter(UserAnswer.user_id == user_id).all()

    # XP: 正解10pt、不正解も挑戦した分2pt
    correct = sum(1 for a in answers if a.is_correct)
    xp = correct * 10 + (len(answers) - correct) * 2
    level = xp // XP_PER_LEVEL + 1
    xp_in_level = xp % XP_PER_LEVEL

    # 日別の回答数（直近70日、JST基準）
    today = datetime.now(JST).date()
    day_counts: dict[date, int] = {}
    for a in answers:
        if a.answered_at is None:
            continue
        d = _to_jst_date(a.answered_at)
        day_counts[d] = day_counts.get(d, 0) + 1

    # 連続学習日数（今日まだ解いていなければ昨日から数える）
    streak = 0
    anchor = today if today in day_counts else today - timedelta(days=1)
    d = anchor
    while d in day_counts:
        streak += 1
        d -= timedelta(days=1)

    activity = []
    for i in range(69, -1, -1):
        d = today - timedelta(days=i)
        activity.append({"date": d.isoformat(), "count": day_counts.get(d, 0)})

    # 直近の最後の回答が不正解のままの問題数（解き直し対象）
    latest: dict[int, UserAnswer] = {}
    for a in sorted(answers, key=lambda x: x.answered_at or datetime.min):
        latest[a.question_id] = a
    mistake_count = sum(1 for a in latest.values() if not a.is_correct)

    return {
        "streak": streak,
        "today_count": day_counts.get(today, 0),
        "daily_goal": DAILY_GOAL,
        "xp": xp,
        "level": level,
        "xp_in_level": xp_in_level,
        "xp_per_level": XP_PER_LEVEL,
        "mistake_count": mistake_count,
        "activity": activity,
    }


@router.get("/{user_id}/sessions")
def get_session_history(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    results = (
        db.query(DiagnosisResult)
        .filter(DiagnosisResult.user_id == user_id)
        .order_by(DiagnosisResult.diagnosed_at.desc())
        .all()
    )

    return [
        {
            "id": r.id,
            "session_id": r.session_id,
            "total_questions": r.total_questions,
            "correct_count": r.correct_count,
            "overall_score": r.overall_score,
            "diagnosed_at": r.diagnosed_at.isoformat() if r.diagnosed_at else None,
        }
        for r in results
    ]


@router.get("/{user_id}/stats")
def get_user_stats(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    total_sessions = db.query(DiagnosisResult).filter(DiagnosisResult.user_id == user_id).count()
    total_answers = db.query(UserAnswer).filter(UserAnswer.user_id == user_id).count()
    correct_answers = db.query(UserAnswer).filter(
        UserAnswer.user_id == user_id, UserAnswer.is_correct == True
    ).count()

    results = (
        db.query(DiagnosisResult)
        .filter(DiagnosisResult.user_id == user_id)
        .order_by(DiagnosisResult.diagnosed_at)
        .all()
    )
    score_history = [
        {
            "score": r.overall_score,
            "date": r.diagnosed_at.isoformat() if r.diagnosed_at else None,
        }
        for r in results
    ]

    latest = results[-1] if results else None
    best = max(results, key=lambda r: r.overall_score) if results else None

    return {
        "user": {
            "id": user.id,
            "username": user.username,
            "display_name": user.display_name,
            "grade": user.grade,
        },
        "total_sessions": total_sessions,
        "total_answers": total_answers,
        "correct_answers": correct_answers,
        "overall_accuracy": round(correct_answers / total_answers * 100, 1) if total_answers > 0 else 0,
        "latest_score": latest.overall_score if latest else None,
        "best_score": best.overall_score if best else None,
        "score_history": score_history,
    }


@router.get("/{user_id}/unit-progress")
def get_unit_progress(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    answers = db.query(UserAnswer).filter(UserAnswer.user_id == user_id).all()

    unit_stats = {}
    for answer in answers:
        question = db.query(Question).filter(Question.id == answer.question_id).first()
        if not question:
            continue

        uid = question.unit_id
        if uid not in unit_stats:
            unit = db.query(Unit).filter(Unit.id == uid).first()
            category = db.query(Category).filter(Category.id == unit.category_id).first() if unit else None
            layer = db.query(Layer).filter(Layer.id == category.layer_id).first() if category else None
            unit_stats[uid] = {
                "unit_code": unit.code if unit else "",
                "unit_name": unit.name if unit else "",
                "category_name": category.name if category else "",
                "layer_name": layer.name if layer else "",
                "total": 0,
                "correct": 0,
            }
        unit_stats[uid]["total"] += 1
        if answer.is_correct:
            unit_stats[uid]["correct"] += 1

    progress = []
    for uid, stats in unit_stats.items():
        score = round(stats["correct"] / stats["total"] * 100, 1) if stats["total"] > 0 else 0
        progress.append({
            **stats,
            "score": score,
            "mastered": score >= 80,
        })

    progress.sort(key=lambda x: x["score"])
    return progress
