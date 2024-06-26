from pydantic import BaseModel


class Tag(BaseModel):
    id: int = None
    title: str
    type: str
