import src.database


def test_filter_expenses(client, setup_database):
    client.post(
        "/expenses",
        json={
            "title": "Test Expense",
            "amount": 100,
            "category": "Food",
        },
    )

    response = client.get("/expenses?category=Food")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["category"] == "Food"
    assert data[0]["amount"] == 100
    assert data[0]["title"] == "Test Expense"
    assert len(src.database.expenses) == 1
    assert src.database.expenses[0].category == "Food"
