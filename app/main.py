from fastapi import FastAPI

from database.database import Base, engine
from router.question_router import questionrouter

HOST = 'localhost'
PORT = 8000

app = FastAPI()
app.include_router(questionrouter)


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


create_tables()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
