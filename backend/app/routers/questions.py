from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Question, Unit, Layer, Category
from ..schemas import QuestionWithExplanation, LayerResponse, CategoryResponse, UnitResponse

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/layers", response_model=list[LayerResponse])
def get_layers(db: Session = Depends(get_db)):
    return db.query(Layer).order_by(Layer.order_priority).all()


@router.get("/categories", response_model=list[CategoryResponse])
def get_categories(layer_id: int = Query(None), db: Session = Depends(get_db)):
    q = db.query(Category)
    if layer_id:
        q = q.filter(Category.layer_id == layer_id)
    return q.order_by(Category.order_priority).all()


@router.get("/units", response_model=list[UnitResponse])
def get_units(category_id: int = Query(None), db: Session = Depends(get_db)):
    q = db.query(Unit)
    if category_id:
        q = q.filter(Unit.category_id == category_id)
    return q.order_by(Unit.order_priority).all()


@router.get("/{question_id}", response_model=QuestionWithExplanation)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    unit = db.query(Unit).filter(Unit.id == question.unit_id).first()

    return {
        "id": question.id,
        "question_text": question.question_text,
        "question_type": question.question_type,
        "difficulty": question.difficulty,
        "explanation": question.explanation,
        "unit_name": unit.name if unit else None,
        "choices": [
            {
                "id": c.id,
                "choice_text": c.choice_text,
                "is_correct": c.is_correct,
                "choice_order": c.choice_order,
            }
            for c in sorted(question.choices, key=lambda c: c.choice_order)
        ],
    }
