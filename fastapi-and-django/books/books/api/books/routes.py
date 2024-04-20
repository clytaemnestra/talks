from fastapi import APIRouter, Depends
from typing import List
from .dependencies import attach_book_service
from .schema import CreateBookRequest, ReadBookSchema
from .services import BookService

router = APIRouter()


@router.get(
    "/", description="Books: Get all books", response_model=List[ReadBookSchema]
)
async def get_all_books(book_service: BookService = Depends(attach_book_service)):
    return await book_service.get_all_books()


@router.get(
    "/{book_id}", description="Books: Get a book by id", response_model=ReadBookSchema
)
async def get_book_by_id(
    book_id: int, book_service: BookService = Depends(attach_book_service)
):
    return await book_service.get_book(book_id)


@router.delete(
    "/{book_id}", description="Books: Delete a book by id", response_model=None
)
async def get_book_by_id(
    book_id: int, book_service: BookService = Depends(attach_book_service)
):
    return await book_service.delete_book(book_id)


@router.post("/", description="Books: Create a new book", response_model=ReadBookSchema)
async def get_book_by_id(
    request: CreateBookRequest, book_service: BookService = Depends(attach_book_service)
):
    return await book_service.create_book(request)
