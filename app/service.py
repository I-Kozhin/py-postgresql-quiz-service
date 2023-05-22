from typing import List

from sqlalchemy.orm import Session  # type: ignore

from .crud import create_question

# requests используется для отправки запросов к внешнему API
import requests

from fastapi import HTTPException

from .schemas import QuestionDtoInput, QuestionDtoOutput  # , Category


def get_one_qiestion_from_api() -> QuestionDtoInput:
    url = f"https://jservice.io/api/random?count={1}"
    response = requests.get(url)
    if response.status_code == 200:
        question_data = response.json()
        question = QuestionDtoInput(
            question_id=question_data[0]['id'],
            answer=question_data[0]['answer'],
            question=question_data[0]['question'],
            created_at=question_data[0]['created_at'],
            airdate=question_data[0]['airdate'],
            updated_at=question_data[0]['updated_at'],
            category_id=question_data[0]['category']['id'],
            game_id=question_data[0]['game_id'],
            invalid_count=question_data[0]['invalid_count']
            # category=Category(
            #     id=question_data[0]['category']['id'],
            #     title=question_data[0]['category']['title'],
            #     created_at=question_data[0]['category']['created_at'],
            #     updated_at=question_data[0]['category']['updated_at'],
            #     clues_count=question_data[0]['category']['clues_count']
            # )
        )
        return question
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch questions from API")


def get_unique_questions(number: int) -> List[QuestionDtoOutput]:
    # question_external = QuestionDtoInput()
    unique_questions = []
    while len(unique_questions) <= number:
        try:
            question_external = get_one_qiestion_from_api()
            print(question_external)
            question_internal = create_question(question_external)
            if question_internal:
                continue
            if not question_internal:
                print('Error till saving in DB')
                continue
            unique_questions.append(question_internal)
        except requests.RequestException:
            print('Error')
            # понять какая ошибка + logging
    return unique_questions
