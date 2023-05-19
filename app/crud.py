from typing import List

from sqlalchemy.orm import Session  # type: ignore

from .models import Question

import requests

from fastapi import HTTPException


def get_random_questions(num_questions: int) -> List[Question] | Question:
    url = f"https://jservice.io/api/random?count={num_questions}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch questions from API")
