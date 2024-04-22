from pydantic import BaseModel


class BaseAuthorSchema(BaseModel):
    name: str
    bio: str = None

    class Config:
        orm_mode = True
        from_attributes = True


class CreateAuthorRequest(BaseAuthorSchema): ...


class ReadAuthorSchema(BaseAuthorSchema):
    id: int
