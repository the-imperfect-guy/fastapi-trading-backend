# 🚀 FastAPI Trading Backend

A production-style backend API built using FastAPI that simulates stock trading with secure authentication and user-specific portfolio tracking.

---

## 🔥 Features

* 📈 Buy & Sell Stocks via REST APIs
* 📊 Portfolio Calculation (Profit/Loss)
* 🔐 JWT Authentication (Signup/Login)
* 🛡️ Protected Routes with Token-based Access
* 👤 User-specific trade isolation
* 🗄️ SQLite Database

---

## 🛠️ Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT (python-jose)
* Passlib (bcrypt)

---

## 📌 API Endpoints

### 🔐 Authentication

* `POST /auth/signup`
* `POST /auth/login`

### 📈 Trading

* `POST /trade` (protected)
* `GET /trade` (protected)
* `GET /trade/portfolio` (protected)

---

## ▶️ Run Locally

```bash
git clone https://github.com/the-imperfect-guy/fastapi-trading-backend.git
cd fastapi-trading-backend

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 📊 Sample Portfolio Output

```json
{
  "AAPL": {
    "quantity": 6,
    "avg_price": 153.33,
    "current_price": 173.33,
    "profit": 120
  }
}
```

---

## 🔐 Authentication Guide

1. Login via `/auth/login`
2. Copy JWT token
3. Click 🔐 Authorize in Swagger
4. Paste token to access protected APIs

---

## 👨‍💻 Author

Shubham Raj
