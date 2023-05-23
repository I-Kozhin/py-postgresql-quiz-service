from fastapi import FastAPI

from database.database import Base, engine
from router.question_router import questionrouter

app = FastAPI()
app.include_router(questionrouter)
Base.metadata.create_all(bind=engine)
