from typing import Optional
from fastapi import APIRouter, HTTPException
from src.models import Expense, ExpenseCreate
import src.services as services

router = APIRouter(prefix="", tags=["Expenses"])

@router.post("/expenses", response_model=Expense)
def create_expense(expense: ExpenseCreate):
    return services.add_expense(expense)

@router.get("/expenses", response_model=list[Expense])
def get_expenses(category: Optional[str] = None):

    if category:
        return services.get_expenses_by_category(category)

    return services.get_all_expenses()

@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    deleted = services.delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {
        "message": "Expense deleted successfully"
    }

@router.get("/expenses/total")
def get_total_expenses():

    return {
        "total": services.calculate_total_expenses()
    }

@router.get("/expenses/total/category")
def get_total_by_category(category: str):
    return {
        "category": category,
        "total": services.calculate_total_by_category(category)
    }
# -------------------------
@router.get("/expenses/search", response_model=list[Expense])
def search_expenses(q: str):
    return services.search_expenses(q)

