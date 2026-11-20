from fastapi import FastAPI

app = FastAPI()


from datetime import datetime
from fastapi import FastAPI
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base, engine

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

app = FastAPI()
