from database import SessionLocal
from models import Book

from fastapi import HTTPException
db = SessionLocal()
def get_books():
    books = db.query(Book).all()
    db.close()
    return books

def get_book_by_id(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    db.close()
    if not book:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    return book

def add_book(title: str, author: str, genre: str):
    new_book = Book(title=title, author=author, genre=genre)
    db.add(new_book)
    db.commit()
    db.close()
    return {"message": "Boek toegevoegd"}

def update_book(book_id: int, title: str, author: str, genre: str):
    db = SessionLocal()
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    book.title = title
    book.author = author
    book.genre = genre
    db.commit()
    db.close()
    return {"message": "Boek bijgewerkt"}

def delete_book(book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Boek niet gevonden")
    db.delete(book)
    db.commit()
    db.close()
    return {"message": "Boek verwijderd"}
