from burnrate.base import Account


def test_account_init():
    """Ensure an Account object can be created."""
    a = Account(name="Evergreen Savings", acct_type="Savings", balance=4300.00)
    assert isinstance(a, Account)
    assert a.name == "Evergreen Savings"
    assert a.acct_type == "Savings"
    assert a.balance == 4300.00


def test_account_balance_float():
    """Ensure the account balance is a float, even when given an int."""
    a = Account(name="First Bank of Armenia", acct_type="Checking", balance=int(5500))
    assert isinstance(a.balance, float)


def test_account_default_balance():
    """Ensure the balance is 0.0 if not specified during creation."""
    a = Account(name="Smells Blargo", acct_type="Checking")
    assert a.balance == 0.0
