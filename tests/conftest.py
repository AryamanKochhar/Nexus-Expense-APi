import pytest
from fastapi.testclient import TestClient
from src.main import app
import src.database as database


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def setup_database():
    database.expenses = []
    database.next_expense_id = 1
