from database.database import SessionLocal


class DatabaseSessionManager:
    @staticmethod
    def get_session():
        session = SessionLocal()
        return session
