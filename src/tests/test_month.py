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
    e2 = Expense(name="Decaf", amount=19, frequency=3)
    m.expenses.extend([e1, e2])
    total = m.total()
    assert total == 22.99 + (19 * 3)
