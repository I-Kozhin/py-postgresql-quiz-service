from fastapi import FastAPI

from app.database.database import init_models
from app.router.question_router import questionrouter
from app.errors import logger
from app.settings import HOST, PORT


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
