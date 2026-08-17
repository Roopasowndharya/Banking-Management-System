"""
=========================================================
SecureBank Console Application
File: exceptions/custom_exceptions.py
Description: Custom Exceptions
=========================================================
"""


class AccountNotFoundError(Exception):
    """Raised when the account is not found."""

    def __init__(self):
        super().__init__("Account not found.")


class InvalidAmountError(Exception):
    """Raised when the amount is invalid."""

    def __init__(self):
        super().__init__("Amount must be greater than zero.")


class InsufficientFundsError(Exception):
    """Raised when balance is insufficient."""

    def __init__(self):
        super().__init__("Insufficient balance.")


class InvalidPINError(Exception):
    """Raised when the PIN is incorrect."""

    def __init__(self):
        super().__init__("Invalid PIN.")


class AccountClosedError(Exception):
    """Raised when the account is closed."""

    def __init__(self):
        super().__init__(" Account is already closed.")