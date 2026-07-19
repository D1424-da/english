import uuid
import json
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..models import Question, Choice, UserAnswer, DiagnosisResult, Unit, Category, Layer
from ..schemas import UnitScore

WEAK_THRESHOLD = 0.6


def start_diagnosis(db: Session, user_id: int, num_questions: int = 20) -> tuple[str, list[Question]]:
    session_id = str(uuid.uuid4())

    questions = (
        db.query(Question)
        .order_by(func.random())
        .limit(num_questions)
        .all()
    )

    return session_id, questions


def submit_answer(db: Session, user_id: int, session_id: str,
                  question_id: int, selected_choice_id: int) -> tuple[bool, int, str | None]:
    correct_choice = (
        db.query(Choice)
        .filter(Choice.question_id == question_id, Choice.is_correct == True)
        .first()
    )

    is_correct = correct_choice and correct_choice.id == selected_choice_id

    answer = UserAnswer(
        user_id=user_id,
        question_id=question_id,
        selected_choice_id=selected_choice_id,
        is_correct=is_correct,
        session_id=session_id,
    )
    db.add(answer)
    db.commit()

    question = db.query(Question).filter(Question.id == question_id).first()
    explanation = question.explanation if question else None

    return is_correct, correct_choice.id if correct_choice else 0, explanation


def calculate_diagnosis(db: Session, user_id: int, session_id: str) -> dict:
    answers = (
        db.query(UserAnswer)
        .filter(UserAnswer.user_id == user_id, UserAnswer.session_id == session_id)
        .all()
    )

    if not answers:
        return None

    total = len(answers)
    correct = sum(1 for a in answers if a.is_correct)
    overall_score = correct / total if total > 0 else 0

    unit_stats: dict[int, dict] = {}
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

    unit_scores = []
    weak_units = []
    for uid, stats in unit_stats.items():
        score = stats["correct"] / stats["total"] if stats["total"] > 0 else 0
        is_weak = score < WEAK_THRESHOLD
        us = UnitScore(
            unit_code=stats["unit_code"],
            unit_name=stats["unit_name"],
            category_name=stats["category_name"],
            layer_name=stats["layer_name"],
            total=stats["total"],
            correct=stats["correct"],
            score=round(score * 100, 1),
            is_weak=is_weak,
        )
        unit_scores.append(us)
        if is_weak:
            weak_units.append(us)

    weak_units.sort(key=lambda u: u.score)

    recommendations = _generate_recommendations(weak_units)

    result = DiagnosisResult(
        user_id=user_id,
        session_id=session_id,
        total_questions=total,
        correct_count=correct,
        overall_score=round(overall_score * 100, 1),
        weak_units=json.dumps([u.unit_code for u in weak_units]),
        recommendations=json.dumps(recommendations, ensure_ascii=False),
    )
    db.add(result)
    db.commit()

    return {
        "session_id": session_id,
        "total_questions": total,
        "correct_count": correct,
        "overall_score": round(overall_score * 100, 1),
        "unit_scores": unit_scores,
        "weak_units": weak_units,
        "recommendations": recommendations,
        "diagnosed_at": result.diagnosed_at,
    }


def _generate_recommendations(weak_units: list[UnitScore]) -> list[str]:
    if not weak_units:
        return ["全体的によくできています。引き続き復習を続けましょう。"]

    recs = []
    for wu in weak_units[:5]:
        if wu.score == 0:
            recs.append(f"【優先度：高】「{wu.unit_name}」({wu.category_name})が全問不正解です。基礎から見直しましょう。")
        elif wu.score < 30:
            recs.append(f"【優先度：高】「{wu.unit_name}」の正答率が{wu.score}%です。教科書の該当箇所を復習しましょう。")
        else:
            recs.append(f"【優先度：中】「{wu.unit_name}」の正答率が{wu.score}%です。問題演習で定着させましょう。")

    if len(weak_units) > 5:
        recs.append(f"他にも{len(weak_units) - 5}個の弱点単元があります。上記を優先的に学習してください。")

    return recs
