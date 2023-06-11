from fastapi import FastAPI

from database.database import init_models
from router.question_router import questionrouter
from app.errors import logger

HOST = '0.0.0.0'
PORT = 8000

app = FastAPI()
app.include_router(questionrouter)


@app.on_event("startup")
async def startup_event():
    try:
        await init_models()
    except Exception as e:
        logger.exception(f'Failed to perform {startup_event} func: {e}')
        raise  # exit


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
