from typing import Optional, List, Union

from pydantic import BaseModel

from database.models.message import Message
from database.tables.messages import Messages


class Messenger(BaseModel):
    id: int = None
    participants: str
    message: Optional[Message] = None
