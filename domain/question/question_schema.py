from pydantic import BaseModel


class Question(BaseModel):
    id: int
    subject: str
    content: str