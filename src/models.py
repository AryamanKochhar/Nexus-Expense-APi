from pydantic import BaseModel
from datetime import datetime
#PYDANTIC IS A LIBRARY FOR VALIDATING DATA, AND CONVERTING DATA TO AND FROM JSON

class Expense(BaseModel):
    id:int
    amount:float
    description:str
    created_at:datetime


class ExpenseCreate(BaseModel):
    amount:float
    description:str
    created_at:datetime

