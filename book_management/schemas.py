from pydantic import BaseModel


class StatusResponse(BaseModel):
    message: str


class BookBase(BaseModel):
    title: str
    author: str
    description: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    model_config = {
        'from_attributes': True
    }

