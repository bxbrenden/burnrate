from dataclasses import dataclass, field
from typing import List, Set

import pandas as pd

MONTHS = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}


@dataclass
class Account:
    name: str
    acct_type: str
    balance: float = 0.0

    def __post_init__(self):
        try:
            self.balance = float(self.balance)
        except TypeError:
            e = f'Invalid type "{type(self.balance)}" for Account: {self}'
            raise SystemExit(e)

    def to_series(self):
        d = {"name": self.name, "acct_type": self.acct_type, "balance": self.balance}
        return pd.Series(data=d, index=[i for i in d.keys()])


@dataclass
class Expense:
    name: str
    amount: float = 0.0
    active: bool = True
    _days_of_month: Set = field(default_factory=lambda: set([1]))

    def __post_init__(self):
        if not isinstance(self._days_of_month, set):
            try:
                self._days_of_month = set(self._days_of_month)
            except TypeError:
                e = f'Invalid type "{type(self._days_of_month)}" for days_of_month'
                raise SystemExit(e)

    @property
    def days_of_month(self):
        return self._days_of_month

    @days_of_month.setter
    def days_of_month(self, new_day):
        try:
            if not isinstance(self._days_of_month, set):
                try:
                    self._days_of_month = set(self._days_of_month)
                except TypeError:
                    e = f'Expense "{self}" has invalid type for _days_of_month'
                    raise SystemExit(e)
            assert isinstance(new_day, int)
            assert new_day in range(1, 32)
            self._days_of_month.add(new_day)
        except AssertionError:
            print("Illegal day of month. Not setting.")

    def total_cost(self, days_in_month=31):
        # days_in_month defaults to 31 since most months have 31 days
        # Some months have 28 or 30 days, so you can change this value
        #    in order to determine whether an expense happens in that month
        if self.active:
            if days_in_month == 31:
                return self.amount * len(self.days_of_month)
            else:
                counted = len(
                    [x for x in self.days_of_month if x in range(1, days_in_month)]
                )
                return self.amount * counted
        else:
            return 0.0

    def __add__(self, other):
        if isinstance(other, Expense):
            return self.total_cost() + other.total_cost()
        elif isinstance(other, float) or isinstance(other, int):
            return self.total_cost() + other

    def __radd__(self, other):
        if other == 0:
            return self.total_cost()
        else:
            return self.__add__(other)

    def __ladd__(self, other):
        if other == 0:
            return self.total_cost()
        else:
            return self.__add__(other)


@dataclass
class Month:
    name: str
    expenses: List[Expense] = field(default_factory=list)
    num_days: int = 31

    def __post_init__(self):
        if self.name not in MONTHS:
            raise SystemExit(f"Invalid month: {self.name}")
        self.num_days = MONTHS[self.name]

    def total(self, num_days=31):
        if num_days == 31:
            return sum(self.expenses)
        else:
            return sum(
                [exp.total_cost(days_in_month=num_days) for exp in self.expenses]
            )


@dataclass
class Year:
    year: int
    months: List[Month] = field(default_factory=list)

    def total(self):
        return sum([month.total() for month in self.months])

    def __post_init__(self):
        for m in MONTHS:
            month = Month(name=m)
            self.months.append(month)


__all__ = ["Account", "Expense", "Month", "Year", "MONTHS"]
