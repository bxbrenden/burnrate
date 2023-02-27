from dataclasses import dataclass, field
from typing import List, Set

from pandas import DataFrame, Series

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
        return Series(data=d, index=[i for i in d.keys()])


@dataclass
class Expense:
    name: str
    amount: float = 0.0
    active: bool = True
    frequency: int = 1

    def __post_init__(self):
        if not isinstance(self.amount, float):
            try:
                self.amount = float(self.amount)
            except TypeError:
                e = f'Invalid type "{type(self.amount)}" for amount'
                raise SystemExit(e)
        if not isinstance(self.frequency, int):
            try:
                self.frequency = int(self.frequency)
            except TypeError:
                e = f'Invalid type "{type(self.frequency)}" for frequency'
                raise SystemExit(e)

    def to_series(self):
        d = {
            "name": self.name,
            "amount": self.amount,
            "active": self.active,
            "frequency": self.frequency,
        }
        return Series(data=d, index=[x for x in d.keys()])

    def total_cost(self):
        if self.active:
            return self.amount * self.frequency
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

    def total(self):
        return sum(self.expenses)

    def to_dataframe(self):
        exp_series_list = [e.to_series() for e in self.expenses]
        return DataFrame(exp_series_list)


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
