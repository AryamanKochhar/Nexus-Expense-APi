# AI Notes

## Tools used

- Cursor (AI coding assistant) for debugging, tests, Docker setup, and README cleanup
- FastAPI / Uvicorn docs and Swagger UI while checking endpoints

## How AI was used

- Fixing import and packaging issues (`ModuleNotFoundError: src`, pytest relative imports)
- Writing / repairing the test suite and `pytest.ini` so `pytest` works from a clean checkout
- Adding the monthly-summary route and Docker (`Dockerfile`, `docker-compose.yml`, `.dockerignore`)
- Aligning the expense model with the required fields: `id`, `title`, `amount`, `category`, `date`
- Drafting README install / run / test commands and verifying them on a clean environment

## What I did myself

- Designed the overall API layout (`routes` / `services` / `models` / in-memory `database`)
- Implemented core expense CRUD, filter, and totals logic
- Ran the server and tests locally, and exercised endpoints in the browser / Swagger

## Bugs and issues faced

1. **Pytest relative imports**  
   Tests used `from .conftest import ...`, which failed with “attempted relative import with no known parent package”. Fixed by using pytest fixtures from `conftest.py` instead of importing it.

2. **Running `python src/main.py`**  
   Failed with `No module named 'src'` because the project root was not on `sys.path`. Fixed by adding the project root to `sys.path` in `main.py` and adding `src/__init__.py`.

3. **Port already in use (`Errno 48`)**  
   Port 8000 was still held by an old process / Docker container. Resolved by stopping the old container/process before starting again.

4. **Root URL 404**  
   `GET /` returns `{"detail":"Not Found"}` because there is no root route. The real entry points are `/docs` and `/expenses`.

5. **Clean-checkout pytest path**  
   Bare `pytest` could not import `src` until `pytest.ini` set `pythonpath = .`.

## What I would improve next

- Persist expenses to a real database or JSON file instead of in-memory storage
- Add authentication and input validation edge cases
- Expand the test suite (search, totals, monthly summary, 404 delete)
