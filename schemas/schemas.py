"""
This file contains the pydantic models for users and PDFs
"""
from pydantic import BaseModel


class UserBase(BaseModel):
    """
    user base model
    """
    firstname: str
    lastname: str
    email: str
    password: str

class UserCreate(UserBase):
    pass