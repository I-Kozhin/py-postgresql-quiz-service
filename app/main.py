from fastapi import FastAPI

from app.database import Base, engine
from app.question_router import questionrouter

app = FastAPI()
app.include_router(questionrouter)
Base.metadata.create_all(bind=engine)
