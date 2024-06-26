from pydantic import BaseModel


class Message(BaseModel):
    id: int = None
    date: str
    time: str
    message: str
    messenger_id: int
    user_id: int
