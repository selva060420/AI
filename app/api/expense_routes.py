from fastapi import APIRouter, HTTPException
from typing import List
from app.models.expense import ExpenseCreate, ExpenseResponse
from app.services.expense_service import expense_service
from app.core.logger import logger

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", response_model=dict)
def add_expense(expense: ExpenseCreate):
    try:
        logger.info(f"Adding expense: {expense.category} - ${expense.amount}")
        result = expense_service.add_expense(expense)
        return result
    except Exception as e:
        logger.error(f"Error adding expense: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=List[dict])
def get_all_expenses():
    try:
        logger.info("Retrieving all expenses")
        expenses = expense_service.get_all_expenses()
        return expenses
    except Exception as e:
        logger.error(f"Error retrieving expenses: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/highest", response_model=dict)
def get_highest_expense():
    try:
        logger.info("Retrieving highest expense")
        expense = expense_service.get_highest_expense()
        if not expense:
            raise HTTPException(status_code=404, detail="No expenses found")
        return expense
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving highest expense: {e}")
        raise HTTPException(status_code=500, detail=str(e))