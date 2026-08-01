#THIS IS A SERVICE FOR THE EXPENSES, should have all the functions to manage the expenses,INTERACTING with db
#: IS for type hinting the data on the left is defined and on the right is the type of the data
from src import database
from src.models import Expense, ExpenseCreate


def add_expense(expense: ExpenseCreate):
    new_expense = Expense(
        id=database.next_expense_id,
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        date=expense.date,
    )
    database.next_expense_id += 1
    database.expenses.append(new_expense)
    return new_expense


def get_all_categories():
    return list(set(expense.category for expense in database.expenses))


def get_all_expenses():
    return database.expenses


def get_expenses_by_category(category: str):
    return [expense for expense in database.expenses if expense.category == category]


def delete_expense(expense_id: int):
    original_len = len(database.expenses)
    database.expenses = [expense for expense in database.expenses if expense.id != expense_id]
    if len(database.expenses) == original_len:
        return None
    return True


def calculate_total_expenses():
    return sum(expense.amount for expense in database.expenses)


def calculate_total_by_category(category: str):
    return sum(expense.amount for expense in database.expenses if expense.category == category)


def search_expenses(query: str):
    return [expense for expense in database.expenses if query in expense.title]


def monthly_summary():  # certain type of ai systems can be implemented to get a summary of all the monthly expenses
    return {
        "total_expenses": calculate_total_expenses(),
        "total_by_category": {
            category: calculate_total_by_category(category) for category in get_all_categories()
        },
    }
