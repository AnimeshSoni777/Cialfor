# main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel


app = FastAPI(title="AI Log Analyzer API")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# The format we expect logs to arrive in
class LogCreate(BaseModel):
    service: str
    level: str
    message: str
    response_time_ms: float

