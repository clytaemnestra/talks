from pydantic import BaseModel, Field


class BookSchema(BaseModel):
    title: str = Field()
    author: str = Field()
    isbn: str = Field()
    publication_date: str | None = Field(default="None")

    class Config:
        orm_mode = True
        from_attributes = True
