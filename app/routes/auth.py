from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas
from app.auth import hash_password, verify_password, create_access_token

# ✅ IMPORTANT: create tables
models.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # ✅ check if user already exists
    existing_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = hash_password(user.password)

    new_user = models.User(
        username=user.username,
        password=hashed
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(
        models.User.username == user.username
    ).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token}