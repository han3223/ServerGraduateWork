from pydantic import BaseModel


class File(BaseModel):
    id: int = None
    file: bytes
