from dataclasses import dataclass
from app import db
from sqlalchemy import Column, Integer, String

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(50), nullable=False)
    dni: str = Column(String(50), nullable=False)
    email: str = Column(String(50), nullable=False)
    gender: str = Column(String(10), nullable=False)
    address: str = Column(String(100), nullable=False)
    phone: str = Column(String(20), nullable=False)
    role: str = Column(String(20), nullable=True)