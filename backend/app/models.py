from sqlalchemy import Column, Integer, String, Text, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from .database import Base


class Layer(Base):
    __tablename__ = "layers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    order_priority = Column(Integer, nullable=False)

    categories = relationship("Category", back_populates="layer")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    layer_id = Column(Integer, ForeignKey("layers.id"), nullable=False)
    order_priority = Column(Integer, nullable=False, default=0)

    layer = relationship("Layer", back_populates="categories")
    units = relationship("Unit", back_populates="category")


class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(20), unique=True, nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    prerequisite_unit_ids = Column(Text)
    order_priority = Column(Integer, nullable=False, default=0)

    category = relationship("Category", back_populates="units")
    questions = relationship("Question", back_populates="unit")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=False)
    question_text = Column(Text, nullable=False)
    question_type = Column(String(50), nullable=False, default="multiple_choice")
    difficulty = Column(Integer, nullable=False, default=1)
    explanation = Column(Text)

    unit = relationship("Unit", back_populates="questions")
    choices = relationship("Choice", back_populates="question")
    user_answers = relationship("UserAnswer", back_populates="question")


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    choice_text = Column(Text, nullable=False)
    is_correct = Column(Boolean, nullable=False, default=False)
    choice_order = Column(Integer, nullable=False, default=0)

    question = relationship("Question", back_populates="choices")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=True)
    display_name = Column(String(100))
    grade = Column(String(20))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    answers = relationship("UserAnswer", back_populates="user")
    diagnosis_results = relationship("DiagnosisResult", back_populates="user")


class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    selected_choice_id = Column(Integer, ForeignKey("choices.id"))
    is_correct = Column(Boolean, nullable=False)
    session_id = Column(String(100))
    answered_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="answers")
    question = relationship("Question", back_populates="user_answers")
    selected_choice = relationship("Choice")


class DiagnosisResult(Base):
    __tablename__ = "diagnosis_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    session_id = Column(String(100), nullable=False)
    total_questions = Column(Integer, nullable=False)
    correct_count = Column(Integer, nullable=False)
    overall_score = Column(Float, nullable=False)
    weak_units = Column(Text)
    recommendations = Column(Text)
    diagnosed_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="diagnosis_results")
