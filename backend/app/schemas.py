from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    display_name: Optional[str] = None
    grade: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    display_name: Optional[str]
    grade: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class ChoiceResponse(BaseModel):
    id: int
    choice_text: str
    choice_order: int

    class Config:
        from_attributes = True


class ChoiceWithAnswer(ChoiceResponse):
    is_correct: bool


class QuestionResponse(BaseModel):
    id: int
    question_text: str
    question_type: str
    difficulty: int
    unit_name: Optional[str] = None
    choices: list[ChoiceResponse]

    class Config:
        from_attributes = True


class QuestionWithExplanation(QuestionResponse):
    explanation: Optional[str]
    choices: list[ChoiceWithAnswer]


class AnswerSubmit(BaseModel):
    question_id: int
    selected_choice_id: int


class AnswerResult(BaseModel):
    question_id: int
    is_correct: bool
    correct_choice_id: int
    explanation: Optional[str]


class DiagnosisStart(BaseModel):
    user_id: int


class WeakPracticeStart(BaseModel):
    user_id: int
    unit_codes: list[str]


class DiagnosisSession(BaseModel):
    session_id: str
    user_id: int
    questions: list[QuestionResponse]
    total_questions: int


class UnitScore(BaseModel):
    unit_code: str
    unit_name: str
    category_name: str
    layer_name: str
    total: int
    correct: int
    score: float
    is_weak: bool


class DiagnosisResultResponse(BaseModel):
    session_id: str
    total_questions: int
    correct_count: int
    overall_score: float
    unit_scores: list[UnitScore]
    weak_units: list[UnitScore]
    recommendations: list[str]
    diagnosed_at: datetime

    class Config:
        from_attributes = True


class LayerResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    order_priority: int

    class Config:
        from_attributes = True


class CategoryResponse(BaseModel):
    id: int
    name: str
    layer_id: int
    order_priority: int

    class Config:
        from_attributes = True


class UnitResponse(BaseModel):
    id: int
    code: str
    name: str
    description: Optional[str]
    category_id: int
    order_priority: int

    class Config:
        from_attributes = True
