"""
fastAPI app
"""
from fastapi import FastAPI
from db.config import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def index():
    return({"message": "Hello world"})