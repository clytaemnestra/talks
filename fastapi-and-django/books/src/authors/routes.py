from fastapi import APIRouter
from typing import List
from .dependencies import AuthorServiceDependency
from .schema import CreateAuthorRequest, ReadAuthorSchema

router = APIRouter()


@router.get(
    "/", description="Authors: Get all authors", response_model=List[ReadAuthorSchema]
)
async def get_all_authors(
    author_service: AuthorServiceDependency,
):
    return await author_service.get_all_authors()


@router.get(
    "/{author_id}",
    description="Authors: Get an author by id",
    response_model=ReadAuthorSchema,
)
async def get_author_by_id(author_id: int, author_service: AuthorServiceDependency):
    return await author_service.get_author(author_id)


@router.delete(
    "/{author_id}", description="Authors: Delete an author by id", response_model=None
)
async def delete_author_by_id(author_id: int, author_service: AuthorServiceDependency):
    return await author_service.delete_author(author_id)


@router.post(
    "/", description="Authors: Create a new author", response_model=ReadAuthorSchema
)
async def create_author(
    request: CreateAuthorRequest, author_service: AuthorServiceDependency
):
    return await author_service.create_author(request)
