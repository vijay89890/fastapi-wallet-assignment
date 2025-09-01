# 💰 FastAPI Wallet Assignment

A simple wallet management API built using **FastAPI**.

---

## 🚀 Setup Instructions

### 1. Clone Repository

git clone https://github.com/your-username/fastapi-wallet-assignment.git
cd fastapi-wallet-assignment

### 2. Create Virtual Environment
bash
Copy code
python -m venv venv
Activate it:

Mac/Linux

bash
Copy code
source venv/bin/activate
Windows

bash
Copy code
venv\Scripts\activate

### 3. Install Dependencies
bash
Copy code
pip install -r requirements.txt

### 4. Run the Application
bash
Copy code
uvicorn main:app --reload
🌐 Access in Browser
Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

📌 API Endpoints
👉 List Users
GET /users
Fetch all users with wallet balance.

👉 Update Wallet
POST /wallet/update
Add or update amount in user’s wallet.

👉 Fetch Transactions
GET /transactions/{user_id}
Fetch all transactions for a specific user.

✨ Tech Stack
FastAPI

SQLite (SQLAlchemy ORM)

Uvicorn

Swagger / ReDoc for API docs





