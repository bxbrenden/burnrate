from pandas import Series

from burnrate.base import Expense


def test_expense_totals():
    """Ensure the Expense.total_cost() method works."""
    e = Expense(name="Manga", amount=7.99)
    assert e.total_cost() == 7.99


def test_expense_totals_multiple_days():
    """Ensure the Expense.total_cost() method works with multiple days."""
    e = Expense(name="Funyuns", amount=3.99, frequency=3)
    assert e.total_cost() == 3.99 * 3


def test_expense_addition_commutative():
    """Ensure that addition is commutative between expenses."""
    e1 = Expense(name="Headphones", amount=50.00)
    e2 = Expense(name="Laptop", amount=800.00)
    radd = e1 + e2
    ladd = e2 + e1
    assert radd == ladd


def test_expense_addition_commutative_multiple():
    """Ensure that addition is commutative between expenses with >1 days."""
    e1 = Expense(name="Gardettos", amount=5.00, frequency=5)
    e2 = Expense(name="Laptop", amount=800.00)
    radd1 = e1 + e2
    ladd1 = e2 + e1
    assert radd1 == ladd1

    e3 = Expense(name="Pencil", amount=3.00)
    e4 = Expense(name="Coffee", amount=3.00)
    radd2 = e3 + e4
    ladd2 = e4 + e3
    assert radd2 == ladd2


def test_expense_summation():
    e1 = Expense(name="Pocket knife", amount=80)
    e2 = Expense(name="Webcam", amount=100)
    expenses = [e1, e2]
    total = e1 + e2
    sum_total = sum(expenses)
    assert total == sum_total


def test_expense_pd_series():
    """Ensure an expense can be converted into a Pandas Series."""
    e1 = Expense(name="Gardettos", amount=5.00, frequency=5)
    s = e1.to_series()
    assert isinstance(s, Series)
