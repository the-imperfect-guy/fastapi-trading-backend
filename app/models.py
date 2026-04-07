from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    stock = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    trade_type = Column(String)
    user = Column(String, index=True) 

from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"

    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)