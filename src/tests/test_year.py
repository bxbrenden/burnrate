from burnrate.base import MONTHS, Year


def test_year_init():
    """Ensure a Year can be instantiated."""
    y = Year(year=2023)
    assert isinstance(y, Year)


def test_year_default_months():
    """Ensure the Year has a list of 12, properly-named, pre-initialized Month objects."""
    y = Year(year=1999)
    name_set = set()
    for month in y.months:
        name_set.add(month.name)

    assert name_set == set([m for m in MONTHS.keys()])
    assert len(name_set) == 12
