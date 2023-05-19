from sqlalchemy.orm import Session  # type: ignore

from .models import Question

from .schemas import QuestionCreate


def get_question_by_id(session: Session, id: int) -> Type[Question] | None:
    return session.query(Question).filter(Question.id == id).first()


def create_question(session: Session, question: QuestionCreate) -> Question:
    new_question = Question(question_text=question.question_text, answer_text=question.answer_text)
    session.add(new_question)
    session.commit()
    session.refresh(new_question)
    return new_question
