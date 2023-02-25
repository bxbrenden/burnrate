from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class Account:
    name: str
    acct_type: str
    balance: float


@dataclass
class Expense:
    name: str
    amount: float = 0.0
    active: bool = True
    days_of_month: Set = field(default_factory=set)
    frequency: int = 1

    def __add__(self, other):
        assert isinstance(other, Expense)
        return self.amount + other.amount

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)


@dataclass
class Month:
    name: str
    expenses: List[Expense] = field(default_factory=list)

    def total(self):
        return sum(self.expenses)


@dataclass
class Year:
    year: int
    months: List[Month] = field(default_factory=list)

    def total(self):
        return sum([month.total() for month in self.months])


__all__ = ["Expense", "Month"]
