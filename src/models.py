from datetime import datetime

from pydantic import BaseModel, Field


class Expense(BaseModel):
    id: int
    amount: float
    description: str
    category: str | None = None
    created_at: datetime


class ExpenseCreate(BaseModel):
    amount: float
    description: str
    category: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
