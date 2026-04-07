from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal, engine
from app.deps import get_current_user

models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/trade", tags=["Trading"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ CREATE TRADE
@router.post("/")
def create_trade(
    trade: schemas.TradeCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    new_trade = models.Trade(**trade.dict(), user=user)
    db.add(new_trade)
    db.commit()
    db.refresh(new_trade)
    return new_trade

# ✅ GET ALL TRADES
@router.get("/")
def get_trades(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return db.query(models.Trade).filter(models.Trade.user == user).all()

# ✅ PORTFOLIO
@router.get("/portfolio")
def get_portfolio(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    trades = db.query(models.Trade).filter(models.Trade.user == user).all()

    portfolio = {}

    for trade in trades:
        stock = trade.stock.upper()

        if stock not in portfolio:
            portfolio[stock] = {
                "quantity": 0,
                "total_cost": 0
            }

        if trade.trade_type == "buy":
            portfolio[stock]["quantity"] += trade.quantity
            portfolio[stock]["total_cost"] += trade.quantity * trade.price

        elif trade.trade_type == "sell":
            portfolio[stock]["quantity"] -= trade.quantity
            portfolio[stock]["total_cost"] -= trade.quantity * trade.price

    result = {}

    for stock, data in portfolio.items():
        if data["quantity"] <= 0:
            continue

        avg_price = data["total_cost"] / data["quantity"]
        current_price = avg_price + 20  
        profit = (current_price - avg_price) * data["quantity"]

        result[stock] = {
            "quantity": data["quantity"],
            "avg_price": round(avg_price, 2),
            "current_price": round(current_price, 2),
            "profit": round(profit, 2)
        }

    return result