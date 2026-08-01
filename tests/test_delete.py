import src.database


def test_delete_expense(client, setup_database):
    create_response = client.post(
        "/expenses",
        json={"amount": 100, "description": "Test Expense"},
    )
    expense_id = create_response.json()["id"]

    response = client.delete(f"/expenses/{expense_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Expense deleted successfully"}
    assert len(src.database.expenses) == 0
