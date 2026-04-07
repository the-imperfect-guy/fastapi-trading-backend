from fastapi import FastAPI
from app.routes import trade

app = FastAPI(title="Trading API 🚀")

app.include_router(trade.router)

@app.get("/")
def home():
    return {"message": "API Running"}


from app.routes import trade, auth

app.include_router(trade.router)
app.include_router(auth.router)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)