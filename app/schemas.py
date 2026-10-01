from pydantic import BaseModel, Field


class MarkEntry(BaseModel):
    subject: str
    score: float = Field(ge=0, le=100)


class Student(BaseModel):
    id: int
    name: str
    marks: list[MarkEntry] = Field(default_factory=list)
