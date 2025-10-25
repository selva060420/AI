# AI

## API Test Application

A simple Python application that demonstrates API consumption.

### Features
- Fetches data from REST API endpoint
- Parses JSON response
- Displays formatted output

### Usage
```bash
python api_test.py
```

### API Endpoint
- URL: https://api.restful-api.dev/objects
- Method: GET
- Response: JSON array of electronic devices

## FastAPI Application

A FastAPI web application that serves the API data.

### Endpoints
- `/` - Hello World message
- `/devices` - Fetches and returns electronic devices from external API
- `POST /expenses` - Add a new expense (category, amount)
- `GET /expenses` - Get all expenses
- `GET /expenses/{id}` - Get expense by ID
- `GET /expenses/stats/highest` - Get highest expense

### Setup
```bash
pip install -r requirements.txt
```

### Run the FastAPI server
```bash
python -m uvicorn main:app --reload
```

### Access
- API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs