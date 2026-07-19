from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..database import get_db
from ..models import DiagnosisResult, UserAnswer, Question, Unit, Category, Layer, User

router = APIRouter(prefix="/history", tags=["history"])


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
