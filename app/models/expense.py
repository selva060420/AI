from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ExpenseCreate(BaseModel):
    category: str
    amount: float
    description: Optional[str] = ""

class ExpenseResponse(BaseModel):
    id: int
    category: str
    amount: float
    description: str
    date_created: datetime