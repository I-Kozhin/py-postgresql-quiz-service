from fastapi import FastAPI

from .database import Base, engine
from .question_router import questionrouter

app = FastAPI()
app.include_router(questionrouter)
Base.metadata.create_all(bind=engine)
