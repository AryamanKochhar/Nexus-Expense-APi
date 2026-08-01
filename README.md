# Nexus Expense API

## What I built

A FastAPI REST API for managing personal expenses.

- Storage: in-memory Python list (data is lost when the server stops)
- Expense fields: `id`, `title`, `amount`, `category`, `date`
- Interactive docs: Swagger UI at `/docs`, ReDoc at `/redoc`

### Core features

- Add an expense
- View all expenses
- Filter expenses by category
- Calculate total expenses (overall and by category)
- Delete an expense

### Optional bonus

- Search expenses by title — `GET /expenses/search?q=Lunch`
- Monthly summary endpoint — `GET /expenses/monthly-summary`
- OpenAPI / Swagger docs — http://localhost:8000/docs (also ReDoc at `/redoc`)
- Docker support — `Dockerfile` and `docker-compose.yml` (see Docker section below)

## Prerequisites

- Python 3
- pip

## Install dependencies

Run these commands from the project root:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows (Command Prompt):

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Start the server

With the virtual environment activated, from the project root:

```bash
python src/main.py
```

The server listens on `http://0.0.0.0:8000`.

Useful URLs:

- Swagger docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- List expenses: http://localhost:8000/expenses

Note: `http://localhost:8000/` has no route and returns `404` with `{"detail":"Not Found"}`. Use `/docs` or `/expenses` instead.

## Run the tests

With the virtual environment activated, from the project root:

```bash
pytest
```

This runs the suite in `tests/` (add, delete, and filter). `pytest.ini` sets `pythonpath = .` so imports resolve correctly.

## Docker (optional)

From the project root:

```bash
docker build -t nexus-expense-api .
docker run -p 8000:8000 nexus-expense-api
```

Or with Compose:

```bash
docker compose up --build
```

If port 8000 is already in use, stop the other process/container first, or map a different host port:

```bash
docker run -p 8001:8000 nexus-expense-api
```

## Project structure

```
.
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── src/
│   ├── main.py
│   ├── routes.py
│   ├── services.py
│   ├── models.py
│   ├── database.py
│   └── utils.py
└── tests/
    ├── conftest.py
    ├── test_add.py
    ├── test_delete.py
    └── test_filter.py
```

## Main endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/expenses` | Create an expense |
| GET | `/expenses` | List all expenses |
| GET | `/expenses?category=Food` | Filter by category |
| DELETE | `/expenses/{expense_id}` | Delete an expense (404 if missing) |
| GET | `/expenses/total` | Overall total (`{"total": ...}`) |
| GET | `/expenses/total/category?category=Food` | Total for one category |
| GET | `/expenses/search?q=Lunch` | Search by title substring |
| GET | `/expenses/monthly-summary` | Totals overall and by category |

### Create an expense

Required JSON fields: `title`, `amount`, `category`.  
Optional: `date` (defaults to the current datetime if omitted).

```bash
curl -X POST http://localhost:8000/expenses \
  -H "Content-Type: application/json" \
  -d '{"title":"Lunch","amount":50,"category":"Food"}'
```

Example response:

```json
{
  "id": 1,
  "title": "Lunch",
  "amount": 50.0,
  "category": "Food",
  "date": "2026-08-01T15:41:08.031663"
}
```
