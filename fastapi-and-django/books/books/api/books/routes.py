from fastapi import APIRouter, Depends
from typing import List
from .dependencies import attach_book_service
from .schema import BookSchema
from .services import BookService

router = APIRouter()


@router.get("/", response_model=List[BookSchema])
async def get_all_books(book_service: BookService = Depends(attach_book_service)):
    return await book_service.get_all_books()
