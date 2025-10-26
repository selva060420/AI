from typing import List, Optional
from mysql.connector import Error
from app.db.database import db_manager
from app.models.expense import ExpenseCreate, ExpenseResponse
from app.core.logger import logger

class ExpenseService:
    
    def add_expense(self, expense: ExpenseCreate) -> dict:
        connection = db_manager.get_connection()
        if not connection:
            logger.error("Failed to get database connection")
            raise Exception("Database connection failed")
        
        try:
            cursor = connection.cursor()
            query = "INSERT INTO expenses (category, amount, description) VALUES (%s, %s, %s)"
            cursor.execute(query, (expense.category, expense.amount, expense.description))
            connection.commit()
            expense_id = cursor.lastrowid
            
            logger.info(f"Expense added successfully with ID: {expense_id}")
            return {"message": "Expense added successfully", "id": expense_id}
            
        except Error as e:
            logger.error(f"Failed to add expense: {e}")
            raise Exception(f"Database error: {e}")
        finally:
            cursor.close()
            connection.close()
    
    def get_all_expenses(self) -> List[dict]:
        connection = db_manager.get_connection()
        if not connection:
            logger.error("Failed to get database connection")
            raise Exception("Database connection failed")
        
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM expenses ORDER BY date_created DESC")
            expenses = cursor.fetchall()
            
            logger.info(f"Retrieved {len(expenses)} expenses")
            return expenses
            
        except Error as e:
            logger.error(f"Failed to retrieve expenses: {e}")
            raise Exception(f"Database error: {e}")
        finally:
            cursor.close()
            connection.close()
    
    def get_highest_expense(self) -> Optional[dict]:
        connection = db_manager.get_connection()
        if not connection:
            logger.error("Failed to get database connection")
            raise Exception("Database connection failed")
        
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM expenses ORDER BY amount DESC LIMIT 1")
            expense = cursor.fetchone()
            
            if expense:
                logger.info(f"Retrieved highest expense: {expense['amount']}")
            else:
                logger.info("No expenses found")
            
            return expense
            
        except Error as e:
            logger.error(f"Failed to retrieve highest expense: {e}")
            raise Exception(f"Database error: {e}")
        finally:
            cursor.close()
            connection.close()

expense_service = ExpenseService()