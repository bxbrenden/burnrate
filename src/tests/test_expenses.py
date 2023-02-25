from burndown.entities import *


def test_expense_totals():
    e = Expense(name="Manga", amount=7.99)
    assert e.total_cost() == 7.99
