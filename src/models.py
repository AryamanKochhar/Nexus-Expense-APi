from datetime import datetime

from pydantic import BaseModel, Field


class Expense(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    date: datetime


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    date: datetime = Field(default_factory=datetime.now)
