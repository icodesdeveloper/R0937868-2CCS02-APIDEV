import models
import schemas
from database import SessionLocal
import models

from fastapi import HTTPException
db = SessionLocal()
def get_books():
    return db.query(models.Book).all()

def get_book_by_id(book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def add_book(book: schemas.BookCreate):
    new_book = models.Book(title=book.title, author=book.author, genre=book.genre)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

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
