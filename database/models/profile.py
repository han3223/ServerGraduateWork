from typing import List

from pydantic import BaseModel


class Profile(BaseModel):
    id: int = None
    lastName: str
    firstName: str
    patronymic: str
    phoneNumber: str
    email: str
    password: str
    image: bytes = None
    tags: str = None
    personalName: str = None
    personalInfo: str = None
    friends: str = None
