"""
db model for PDFs
"""


from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from db.config import Base
from .user import User

class PDF(Base):
    """
    pdf model
    """
    __tablename__ = "pdfs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    file = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship(User, back_populates="pdfs")
