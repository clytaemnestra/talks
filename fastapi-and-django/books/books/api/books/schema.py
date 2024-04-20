from datetime import date

from pydantic import BaseModel, Field


class BaseBookSchema(BaseModel):
    title: str
    author: str
    isbn: str
    publication_date: date

    class Config:
        orm_mode = True
        from_attributes = True


class CreateBookRequest(BaseBookSchema): ...


class ReadBookSchema(BaseBookSchema):
    id: int = Field()
