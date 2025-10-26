from fastapi import FastAPI
from app.api.expense_routes import router as expense_router
from app.db.database import db_manager
from app.core.logger import logger

app = FastAPI(
    title="Personal Expense Tracker API",
    description="A FastAPI application for tracking personal expenses",
    version="1.0.0"
)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Personal Expense Tracker API")
    db_manager.create_database_and_table()

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Personal Expense Tracker API", "version": "1.0.0"}

app.include_router(expense_router)