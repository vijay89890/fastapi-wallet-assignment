from pydantic import BaseModel
from typing import List
from datetime import datetime


# This will define what a User looks like when returned in API
class UserBase(BaseModel):
    name: str
    email: str
    phone: str
    wallet_balance: float

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    amount: float
    timestamp: datetime

    class Config:
        orm_mode = True

class WalletUpdate(BaseModel):
    user_id: int
    amount: float
