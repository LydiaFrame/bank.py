
"""transactions.py - Handles deposit, withdrawal, and interest calculations for a bank account."""

balance = 0.0

def deposit(amount):
    """Adds an amount to the balance.
    
    Args:
        amount (float): The amount to deposit.

    Returns:
        float: The updated balance.
    """
    global balance
    balance += amount
    return balance


def withdraw(amount):
    """Removes an amount from the balance.
    
    Args:
        amount (float): The amount to withdraw.

    Returns:
        float: The updated balance.
    """
    global balance
    balance -= amount
    return balance


def apply_interest(rate):
    """Applies interest to the balance.
    
    Args:
        rate (float): The interest rate as a percentage.

    Returns:
        float: The updated balance after applying interest.
    """
    global balance
    interest_amount = balance * (rate / 100)
    balance += interest_amount
    return balance