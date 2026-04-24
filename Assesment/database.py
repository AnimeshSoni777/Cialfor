# database.py
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Creates a local file called logs.db
engine = create_engine("sqlite:///./logs.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class LogEntry(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    response_time_ms = Column(Float)
    message = Column(String)
    anomaly_score = Column(Float, nullable=True)
    is_anomaly = Column(Boolean, default=False)

# Create the tables
Base.metadata.create_all(bind=engine)