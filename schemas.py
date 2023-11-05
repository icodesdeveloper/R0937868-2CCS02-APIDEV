from pydantic import BaseModel
class BookBase(BaseModel):
    id:int
    title: str
    author: str
    genre: str

class BookCreate(BookBase):
    title: str
    author: str
    genre: str