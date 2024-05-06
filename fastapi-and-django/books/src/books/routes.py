from fastapi import APIRouter
from typing import List
from .dependencies import BookServiceDependency
from .schema import CreateBookRequest, ReadBookSchema

router = APIRouter()


@router.get(
    "/", description="Books: Get all books", response_model=List[ReadBookSchema]
)
async def get_all_books(book_service: BookServiceDependency):
    return await book_service.get_all_books()


@router.get(
    "/{book_id}", description="Books: Get a book by id", response_model=ReadBookSchema
)
async def get_book_by_id(book_id: int, book_service: BookServiceDependency):
    return await book_service.get_book(book_id)


@router.delete(
    "/{book_id}", description="Books: Delete a book by id", response_model=None
)
async def delete_book_by_id(book_id: int, book_service: BookServiceDependency):
    return await book_service.delete_book(book_id)


@router.post("/", description="Books: Create a new book", response_model=ReadBookSchema)
async def create_new_book(
    request: CreateBookRequest, book_service: BookServiceDependency
):
    return await book_service.create_book(request)
