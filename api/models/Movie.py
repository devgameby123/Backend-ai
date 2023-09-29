from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    name: str
    image: bytes
    category: str
