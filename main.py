from fastapi import FastAPI
from database import Base, engine
from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from sqlalchemy.orm import Session
from models import User, Transaction   




app = FastAPI(title="Wallet API", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}


# Create the database tables
Base.metadata.create_all(bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users", response_model=list[schemas.UserBase])
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

with SessionLocal() as db:
    if not db.query(models.User).first():  # only if table empty
        user1 = models.User(name="Vijay", email="vijay@gmail.com", phone="9999999999", wallet_balance=500)
        user2 = models.User(name="Ankit", email="ankit@gmail.com", phone="8888888888", wallet_balance=200)
        db.add_all([user1, user2])
        db.commit()

@app.post("/wallet/update")
def update_wallet(wallet: schemas.WalletUpdate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == wallet.user_id).first()

    if not user:
        return {"error": "User not found"}

    # Update wallet balance
    user.wallet_balance += wallet.amount

    # Add a transaction record
    transaction = models.Transaction(user_id=user.id, amount=wallet.amount)
    db.add(transaction)

    db.commit()
    db.refresh(user)

    return {
        "message": "Wallet updated successfully",
        "new_balance": user.wallet_balance
    }

@app.get("/transactions/{user_id}")
def get_transactions(user_id: int, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()

    return [
        {
            "id": txn.id,
            "amount": txn.amount,
            "timestamp": txn.timestamp
        }
        for txn in transactions
    ]