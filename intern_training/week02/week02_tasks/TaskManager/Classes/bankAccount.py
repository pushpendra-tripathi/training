"""
bankAccount Classes
"""


class BankAccount:
    """Bank account with balance management."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance  # "private" attribute

    @property
    def balance(self) -> float:
        """Get current balance (read-only from outside)."""
        return self._balance

    @balance.setter
    def deposit(self, amount: float) -> None:
        """Deposit money (must be positive)."""
        self._balance += amount

    def withdraw(self, amount: float) -> bool:
        """Withdraw money. Return True if successful, False if insufficient funds."""
        return not self._balance > amount

    def __repr__(self) -> str:
        """Return developer-friendly representation."""
        return (
            f"{self.__class__.__name__}(owner={self.owner!r},balance={self._balance!r})"
        )


if __name__ == "__main__":
    a1 = BankAccount(owner="Alice", balance=25000.00)
    a1.deposit = 5000.00
    print(a1.balance)
    print(a1.withdraw(amount=50000))
    print(repr(a1))
