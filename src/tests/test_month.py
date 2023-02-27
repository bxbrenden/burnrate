from burndown.base import Month


def test_month_init():
    """Ensure Month objects can be instantiated."""
    m = Month(name="January")
    assert isinstance(m, Month)
