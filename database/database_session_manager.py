from sqlalchemy.orm import Session
from database.database import SessionLocal


class DatabaseSessionManager:
    @staticmethod
    def get_session() -> Session:
        session = SessionLocal()
        return session
