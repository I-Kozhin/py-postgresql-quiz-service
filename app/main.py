import asyncio

import typer
from fastapi import FastAPI

from database.database import init_models
from router.question_router import questionrouter

HOST = 'localhost'
PORT = 8000

app = FastAPI()
app.include_router(questionrouter)
cli = typer.Typer()


@app.on_event("startup")
async def startup_event():
    await init_models()


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
