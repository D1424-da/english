from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import User, Unit
from ..schemas import (
    DiagnosisStart, DiagnosisSession, QuestionResponse,
    AnswerSubmit, AnswerResult, DiagnosisResultResponse,
)
from ..services.diagnosis_service import start_diagnosis, submit_answer, calculate_diagnosis

router = APIRouter(prefix="/diagnosis", tags=["diagnosis"])


@router.post("/start", response_model=DiagnosisSession)
def start_diagnosis_session(req: DiagnosisStart, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == req.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    session_id, questions = start_diagnosis(db, req.user_id)

    question_list = []
    for q in questions:
        unit = db.query(Unit).filter(Unit.id == q.unit_id).first()
        question_list.append(QuestionResponse(
            id=q.id,
            question_text=q.question_text,
            question_type=q.question_type,
            difficulty=q.difficulty,
            unit_name=unit.name if unit else None,
            choices=[
                {"id": c.id, "choice_text": c.choice_text, "choice_order": c.choice_order}
                for c in sorted(q.choices, key=lambda c: c.choice_order)
            ],
        ))

    return DiagnosisSession(
        session_id=session_id,
        user_id=req.user_id,
        questions=question_list,
        total_questions=len(question_list),
    )


@router.post("/answer", response_model=AnswerResult)
def submit_answer_endpoint(
    session_id: str,
    user_id: int,
    answer: AnswerSubmit,
    db: Session = Depends(get_db),
):
    is_correct, correct_id, explanation = submit_answer(
        db, user_id, session_id, answer.question_id, answer.selected_choice_id
    )

    return AnswerResult(
        question_id=answer.question_id,
        is_correct=is_correct,
        correct_choice_id=correct_id,
        explanation=explanation,
    )


@router.post("/result", response_model=DiagnosisResultResponse)
def get_diagnosis_result(session_id: str, user_id: int, db: Session = Depends(get_db)):
    result = calculate_diagnosis(db, user_id, session_id)
    if not result:
        raise HTTPException(status_code=404, detail="No answers found for this session")

    return result
