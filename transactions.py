from decimal import Decimal, InvalidOperation
from typing import List, Tuple

# Constants
CURRENCY_SYMBOL = "R"
# TODO: Remove the TRANSACTION_TYPES constant below - we are not using it in the Transaction class


class Transaction:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        try:
            self.amount = Decimal(amount)
        except InvalidOperation:
            raise ValueError(f"Invalid amount: {amount}")
        self.category = category

    def __repr__(self):
        return f"Transaction(date='{self.date}', description='{self.description}', amount={self.amount}, category='{self.category}')"


# TODO: Implement this function to sum all transactions with negative amounts
def calculate_total_expenses(transactions: List[Transaction]) -> Decimal:
    """Calculates the total expenses from a list of transactions.

    Args:
        transactions: A list of Transaction objects.

    Returns:
        The total expenses as a Decimal (should be negative).
    Example:
        >>> transactions = [Transaction('2024-01-01', 'Groceries', '-500.00', 'Food'),
        ...                 Transaction('2024-01-02', 'Rent', '-1500.00', 'Housing')]
        >>> calculate_total_expenses(transactions)
        Decimal('-2000.00')
    """
    # Code deleted as requested


# TODO: Implement this function to sum all transactions with positive amounts
def calculate_total_income(transactions: List[Transaction]) -> Decimal:
    """Calculates the total income from a list of transactions.

    Args:
        transactions: A list of Transaction objects.

    Returns:
        The total income as a Decimal (should be positive).
    """
    total = Decimal(0)

    for transaction in transactions:
        if transaction.amount > 0:
            total += transaction.amount

    return total


# NOTE: This function is already complete - no changes needed here!
def format_currency(amount: Decimal) -> str:
    """
    Format a numeric amount as South African Rand currency.

    Args:
        amount: The amount to format as a float or Decimal.

    Returns:
        A formatted string with the Rand symbol and two decimal places.

    Example:
        >>> format_currency(Decimal("1234.56"))
        'R 1234.56'
    """
    return f"{CURRENCY_SYMBOL} {amount:,.2f}"


# TODO: Remove the entire add_transaction function below (no longer needed with Transaction class)


# TODO: Update this function to work with Transaction objects instead of dicts.
# Change List[dict] to List[Transaction], use dot notation (t.amount), and update docstring.
# Hint: With Transaction objects, simply sum all amounts (expenses are negative, income is positive)!
def calculate_balance(transactions: List[dict]) -> Decimal:
    """
    Calculate the current balance from a list of transactions.

    Income transactions add to the balance; expense transactions subtract.

    Args:
        transactions: A list of transaction dictionaries.

    Returns:
        The calculated balance as a Decimal.

    Example:
        >>> transactions = [
        ...     {"amount": Decimal("5000"), "type": "income"},
        ...     {"amount": Decimal("1000"), "type": "expense"}
        ... ]
        >>> calculate_balance(transactions)
        Decimal('4000')
    """
    balance = Decimal(0)
    balance = calculate_total_income(transactions) + calculate_total_expenses(
        transactions
    )
    return balance


# TODO: Remove the entire get_income_total function below (replaced by calculate_total_income)


# TODO: Remove the entire get_expense_total function below (replaced by calculate_total_expenses)


# TODO: Remove the entire check_budget function below (not needed for this tutorial)


# TODO: Remove the entire display_transactions function below (not needed for this tutorial)


# TODO: Remove the entire if __name__ == "__main__": block below (old example code)
if __name__ == "__main__":
    # Example usage
    transactions = []
    add_transaction(transactions, "Salary", Decimal("5000"), "income")
    add_transaction(transactions, "Groceries", Decimal("1500"), "expense")
    add_transaction(transactions, "Freelance", Decimal("2000"), "income")
    add_transaction(transactions, "Rent", Decimal("2500"), "expense")

    display_transactions(transactions)

    balance = calculate_balance(transactions)
    print(f"\nCurrent Balance: {format_currency(balance)}")

    budget_limit = Decimal("3000")
    within_budget, message = check_budget(balance, budget_limit)
    print(message)
