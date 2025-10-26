# Personal Expense Tracker API

A FastAPI application for tracking personal expenses with MySQL database integration.

## Project Structure
```
ai/
├── app/
│   ├── api/
│   │   └── expense_routes.py    # API endpoints
│   ├── core/
│   │   ├── config.py           # Configuration settings
│   │   └── logger.py           # Logging configuration
│   ├── db/
│   │   └── database.py         # Database connection manager
│   ├── models/
│   │   └── expense.py          # Pydantic models
│   ├── services/
│   │   └── expense_service.py  # Business logic layer
│   └── __init__.py
├── logs/                       # Application logs
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Dependencies
└── README.md
```

## Features
- Clean architecture with separation of concerns
- Comprehensive logging to files and console
- Environment-based configuration
- Proper error handling
- MySQL database integration
- RESTful API design

## Prerequisites
- Python 3.8+
- MySQL Server running on localhost
- MySQL credentials: root/Selva@0604

## Database Configuration
- Host: localhost
- User: root
- Password: Selva@0604
- Database: expense_tracker (auto-created)

## Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Application
```bash
python -m uvicorn main:app --reload
```

### 3. Alternative Start Commands
```bash
# Basic start
python -m uvicorn main:app

# With specific host and port
python -m uvicorn main:app --host 0.0.0.0 --port 8000

# Development mode with auto-reload
python -m uvicorn main:app --reload --port 8000
```

## API Endpoints

### 1. Root Endpoint
- **GET** `/` - API information

### 2. Expense Management
- **POST** `/expenses/` - Add new expense
- **GET** `/expenses/` - Get all expenses
- **GET** `/expenses/highest` - Get highest expense

## API Testing

### Sample POST Request (Add Expense)
```json
{
    "category": "Food",
    "amount": 25.50,
    "description": "Lunch at restaurant"
}
```

### Test Data Examples
```json
// Expense 1
{
    "category": "Food",
    "amount": 25.50,
    "description": "Lunch at restaurant"
}

// Expense 2
{
    "category": "Transportation",
    "amount": 15.00,
    "description": "Bus fare"
}

// Expense 3
{
    "category": "Entertainment",
    "amount": 45.99,
    "description": "Movie tickets"
}
```

### Testing Sequence
1. **Test Root:** GET `http://localhost:8000/`
2. **Add Expenses:** POST to `/expenses/` with sample data
3. **Get All:** GET `/expenses/` to verify data
4. **Get Highest:** GET `/expenses/highest` to get maximum expense

## Access Points
- **API Base:** http://localhost:8000
- **Interactive Docs:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc
- **Logs:** `logs/app_YYYYMMDD.log`

## Troubleshooting

### Virtual Environment Issues
```bash
# Create new venv
python -m venv venv

# Activate (PowerShell)
venv\Scripts\Activate.ps1

# Activate (CMD)
venv\Scripts\activate.bat
```

### Database Connection
- Ensure MySQL server is running
- Verify credentials: root/Selva@0604
- Database and table are auto-created on startup

### Application Logs
- Check `logs/app_YYYYMMDD.log` for detailed error information
- Console output shows real-time application status

## Development Notes
- Application auto-creates database and tables on startup
- Logs are written to both file and console
- Use `--reload` flag for development to auto-restart on code changes
- Stop application with `Ctrl+C`