from typing import List, Optional

import aiohttp
from sqlalchemy.orm import Session  # type: ignore
from sqlalchemy.ext.asyncio import AsyncSession
from dto.question_dto import QuestionDto
from repositories.question_repository import QuestionRepository


class QuestionServiceError(Exception):
    pass


class QuestionApiService:
    @staticmethod
    async def get_unique_questions_from_api(question_count: int) -> List[QuestionDto]:
        unique_questions_from_api = []
        while len(unique_questions_from_api) < question_count:
            url = f"https://jservice.io/api/random?count={1}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        question_data = await response.json()
                        question = QuestionDto.parse_obj(question_data[0])
                        unique_questions_from_api.append(question)
                    else:
                        raise QuestionServiceError(f"Failed to fetch questions from API: {response.status}")

        return unique_questions_from_api


class QuestionService:
    question_repository: QuestionRepository
    question_api_service: QuestionApiService

    def __init__(self):
        self.question_repository = QuestionRepository()
        self.question_api_service = QuestionApiService()

    async def create_unique_questions(self, question_count: int, session: AsyncSession) -> None:
        unique_questions = await self.question_api_service.get_unique_questions_from_api(question_count)
        await self.question_repository.create_questions(unique_questions, session)

    async def get_last_question(self, session: AsyncSession) -> Optional['Question']:
        return await self.question_repository.get_last_question_nullable(session)
