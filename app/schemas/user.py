from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: str


    class Config():
        orm_mode = True
