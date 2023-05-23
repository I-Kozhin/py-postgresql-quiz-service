# requests используется для отправки запросов к внешнему API
from typing import List

import requests
from sqlalchemy.orm import Session  # type: ignore

from crud.question_repository import QuestionRepository
from dto.question_dto import QuestionDto


class QuestionServiceError(Exception):
    pass


class QuestionService:
    question_repository: QuestionRepository

    def __init__(self):
        self.question_repository = QuestionRepository()

    def create_unique_questions(self, question_count: int) -> None:
        unique_questions = self.__get_unique_questions_from_api(question_count)
        self.question_repository.create_questions(unique_questions)

    def get_last_question(self):
        return self.question_repository.get_last_question_nullable()

    def __get_unique_questions_from_api(self, question_count: int) -> List[QuestionDto]:
        unique_questions_from_api = []
        while len(unique_questions_from_api) < question_count:
            url = f"https://jservice.io/api/random?count={1}"
            response = requests.get(url)
            if response.status_code == 200:
                question_data = response.json()
                question = QuestionDto.parse_obj(question_data[0])
                #  есть ли вопрос в бд
                if self.question_repository.is_question_exist(question.question):
                    continue
                else:
                    unique_questions_from_api.append(question)
            else:
                raise QuestionServiceError(f"Failed to fetch questions from API: {response.status_code}")

        return unique_questions_from_api
