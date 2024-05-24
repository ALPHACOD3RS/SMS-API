from pydantic import BaseModel, EmailStr
from typing import List


class StudentBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    date_of_birth: date
    address: str
    class_id: int
    
    
    