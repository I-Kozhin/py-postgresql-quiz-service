from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session  # type: ignore

from . import models
from .crud import get_question_by_id, create_question
from .database import SessionLocal, engine
from .models import Question
from .schemas import QuestionCreate

models.Base.metadata.create_all(bind=engine)
questionrouter = APIRouter()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@questionrouter.get("/questions/{id}", response_model=Question)
def get_question(id: int, session: Session = Depends(SessionLocal)):
    question = get_question_by_id(session, id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@questionrouter.post("/questions/", response_model=Question)
def create_question_api(question: QuestionCreate, session: Session = Depends(SessionLocal)):
    return create_question(session, question)
