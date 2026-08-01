import src.database


def test_add_expense(client, setup_database):
    response = client.post(
        "/expenses",
        json={"amount": 100, "description": "Test Expense"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 100
    assert data["description"] == "Test Expense"
    assert data["id"] == 1
    assert len(src.database.expenses) == 1
    assert src.database.expenses[0].amount == 100
    assert src.database.expenses[0].description == "Test Expense"
