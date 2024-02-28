"""
User database model
"""


from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

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

    pdfs = relationship("PDF", back_populates="user")


class PDF(Base):
    """
    pdf model
    """
    __tablename__ = "pdfs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    file = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="pdfs")
