from fastapi import FastAPI
from crud import get_books, get_book_by_id, add_book, update_book, delete_book
import models

app = FastAPI()

# Endpoint om alle boeken op te halen
@app.get("/books")
async def get_all_books():
    return get_books()

@app.get("/books/{book_id}")
async def get_book_by_id_endpoint(book_id: int):
    return get_book_by_id(book_id)

@app.post("/books")
async def add_new_book(title: str, author: str, genre: str):
    return add_book(title, author, genre)

@app.put("/books/{book_id}")
async def update_existing_book(book_id: int, title: str, author: str, genre: str):
    return update_book(book_id, title, author, genre)

@app.delete("/books/{book_id}")
async def delete_existing_book(book_id: int):
    return delete_book(book_id)
