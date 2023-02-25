class Expense:
    def __init__(self, name, account, amount=0.0, active=True, days_of_month=[1], frequency=1):
        pass


class Month:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def total(self):
        return sum(self.expenses)

__all__ = ['Expense', 'Month']
