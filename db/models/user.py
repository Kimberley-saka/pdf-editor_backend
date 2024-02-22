"""
User database model
"""


from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .pdf import PDF
from db.config import Base

class User(Base):
    """
    User class
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    pdfs = relationship(PDF, back_populates="user")
