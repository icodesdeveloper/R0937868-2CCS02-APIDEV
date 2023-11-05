from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, schemas, models
from database import get_db

app = FastAPI()

# Endpoint om alle boeken op te halen
@app.get("/books")
async def get_all_books():
    return get_books()

@app.get("/books/{book_id}")
async def get_book_by_id_endpoint(book_id: int):
    return get_book_by_id(book_id)

@app.post("/books")
def create_book(book: schemas.BookCreate):
    return add_book(book)

@app.put("/books/{book_id}")
async def update_existing_book(book_id: int, title: str, author: str, genre: str):
    return update_book(book_id, title, author, genre)

@app.delete("/books/{book_id}")
async def delete_existing_book(book_id: int):
    return delete_book(book_id)
