
from sqlalchemy.orm import Session

import models
import schemas

from fastapi import HTTPException
def get_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_id(db: Session, book_id: int):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book



def add_book(db: Session, book: schemas.BookCreate):
    new_book = models.Book(title=book.title, author=book.author, genre=book.genre)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def delete_book(db: Session, book_id: int):
    existing_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if existing_book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(existing_book)
    db.commit()

    return {"message": "Book deleted successfully"}
