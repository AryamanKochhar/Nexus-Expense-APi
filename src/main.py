import sys
from pathlib import Path
# Allow running as: python3 src/main.py (project root must be on sys.path)
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from fastapi import FastAPI
import uvicorn

from src.routes import router

app = FastAPI(
    title="Nexus Expense API",
    description="A simple REST API to manage personal expenses.",
    version="1.0.0"
)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
