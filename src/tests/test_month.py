from burnrate.base import MONTHS, Expense, Month


def test_month_init():
    """Ensure Month objects can be instantiated."""
    m = Month(name="January")
    assert isinstance(m, Month)


def test_invalid_month():
    """Make sure no invalidly named Month objects can be made."""
    try:
        m = Month(name="Smarch")
    except SystemExit:
        assert 1 == 1


def test_month_total():
    """Ensure months can sum their total expenses."""
    m = Month(name="March")
    e1 = Expense(name="NA Beer", amount=22.99)
    e2 = Expense(name="Decaf", amount=19, _days_of_month=[1, 15, 30])
    m.expenses.extend([e1, e2])
    total = m.total()
    assert total == 22.99 + (19 * 3)


def test_short_month():
    """Ensure an expense that happens on the 31st day won't be counted in e.g. February"""
    m = Month(name="February")
    e = Expense(name="Plywood", amount=15.00, _days_of_month=[1, 15, 31])
    m.expenses.append(e)
    total = m.total(num_days=28)
    assert total == 30.00
