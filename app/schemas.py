from pydantic import BaseModel

class TradeCreate(BaseModel):
    stock: str
    quantity: int
    price: float
    trade_type: str

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str