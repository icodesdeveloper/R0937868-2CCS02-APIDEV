from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint om alle boeken op te halen
@app.get("/books/")
async def get_all_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.post("/books/")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.add_book(db, book)
@app.get("/books/{book_id}")
def get_book_by_id_endpoint(book_id: int, db: Session = Depends(get_db)):
    return crud.get_book_by_id(db, book_id)

@app.delete("/books/{book_id}")
async def delete_existing_book(book_id: int, db: Session = Depends(get_db)):
    return crud.delete_book(db, book_id)
