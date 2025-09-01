Here’s a clean template tailored to your Wallet API Assignment:

# 💰 FastAPI Wallet Assignment

This project is a simple **Wallet Management API** built using **FastAPI** and **SQLAlchemy**.  
It allows you to:  
- List all users and their wallet balances  
- Update (credit/debit) a user’s wallet  
- Fetch all transactions for a specific user  

All APIs are automatically documented with **Swagger UI** (`/docs`).

---

## 🚀 Features
1. **List Users API** – Fetch all users with details (name, email, phone, wallet balance).  
2. **Update Wallet API** – Add or update wallet balance for a user.  
3. **Fetch Transactions API** – Fetch all wallet transactions for a given user.  

---

## 🛠 Tech Stack
- [FastAPI](https://fastapi.tiangolo.com/) – Framework  
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM for database  
- [SQLite](https://www.sqlite.org/) – Database  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/fastapi-wallet-assignment.git
cd fastapi-wallet-assignment

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
uvicorn main:app --reload


Now open in browser:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📌 API Endpoints
👉 List Users

GET /users

👉 Update Wallet

POST /users/{user_id}/wallet

{
  "amount": 100.5,
  "type": "credit"   // or "debit"
}

👉 Fetch Transactions

GET /users/{user_id}/transactions
