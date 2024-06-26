from typing import List

from pydantic import BaseModel


class Document(BaseModel):
    id: int = None
    title: str
    category: str
    file_id: int
    date: str
    image: str = None
    user_id: int
    tags: str
    description: str = None
