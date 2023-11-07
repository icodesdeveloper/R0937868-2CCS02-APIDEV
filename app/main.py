from fastapi import Depends, FastAPI, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
import secrets
import crud
import models
import schemas
from database import SessionLocal, engine
import os

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
security = HTTPBasic()
models.Base.metadata.create_all(bind=engine)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"!kun0"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"$2a$12$L6VwhYGP.gSNPnNAXKPAJe93fOGhKL/IA6t1x.BZgkT2vJ3GDzrZa" #Use a hashed password here
    is_correct_password = pwd_context.verify(current_password_bytes, correct_password_bytes)
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


# Endpoint om alle boeken op te halen
@app.get("/books/")
async def get_all_books(db: Session = Depends(get_db), username: str = Depends(get_current_username)):
    return crud.get_books(db)

@app.post("/books/")
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db), username: str = Depends(get_current_username)):
    return crud.add_book(db, book)
@app.get("/books/{book_id}")
def get_book_by_id_endpoint(book_id: int, db: Session = Depends(get_db), username: str = Depends(get_current_username)):
    return crud.get_book_by_id(db, book_id)

@app.delete("/books/{book_id}")
async def delete_existing_book(book_id: int, db: Session = Depends(get_db), username: str = Depends(get_current_username)):
    return crud.delete_book(db, book_id)
