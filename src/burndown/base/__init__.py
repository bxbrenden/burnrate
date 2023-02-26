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
    _days_of_month: Set = field(default_factory=lambda: set([1]))

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

    def total_cost(self):
        if self.active:
            return self.amount * len(self.days_of_month)
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

    def total(self):
        return sum(self.expenses)


@dataclass
class Year:
    year: int
    months: List[Month] = field(default_factory=list)

    def total(self):
        return sum([month.total() for month in self.months])


__all__ = ["Account", "Calendar", "Expense", "Month", "Year"]
