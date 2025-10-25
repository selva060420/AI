from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import urllib.request
import json

app = FastAPI()
expenses = []

class Expense(BaseModel):
    category: str
    amount: float

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/devices")
def get_devices():
    response = urllib.request.urlopen('https://api.restful-api.dev/objects')
    data = json.loads(response.read())
    return data

@app.post("/expenses")
def add_expense(expense: Expense):
    expense_data = expense.dict()
    expense_data["id"] = len(expenses) + 1
    expenses.append(expense_data)
    return {"message": "Expense added", "expense": expense_data}

@app.get("/expenses")
def get_expenses():
    return expenses

@app.get("/expenses/{expense_id}")
def get_expense_by_id(expense_id: int):
    for expense in expenses:
        if expense["id"] == expense_id:
            return expense
    raise HTTPException(status_code=404, detail="Expense not found")

@app.get("/expenses/stats/highest")
def get_highest_expense():
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found")
    highest = max(expenses, key=lambda x: x["amount"])
    return highest