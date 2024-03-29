"""
Database Configurations
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLACHEMY_DATABASE_URL = "postgresql://postgres:postgres@postgresserver/pdfeditor"

engine  = create_engine(SQLACHEMY_DATABASE_URL) # Connect to the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()