import src.database


def test_add_expense(client, setup_database):
    response = client.post(
        "/expenses",
        json={"title": "Test Expense", "amount": 100, "category": "Food"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Expense"
    assert data["amount"] == 100
    assert data["category"] == "Food"
    assert data["id"] == 1
    assert "date" in data
    assert len(src.database.expenses) == 1
    assert src.database.expenses[0].title == "Test Expense"
    assert src.database.expenses[0].amount == 100
