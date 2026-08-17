"""
=========================================================
SecureBank Console Application
File: utils/validator.py
Description: Input Validation Functions
=========================================================
"""

from exceptions.custom_exceptions import InvalidAmountError


class Validator:
    """
    Contains validation methods for SecureBank.
    """

    @staticmethod
    def validate_name(name):
        """
        Validate customer name.
        """
        if not name.strip():
            raise ValueError("Customer name cannot be empty.")

        if len(name) < 3:
            raise ValueError("Customer name must contain at least 3 characters.")

        if not name.replace(" ", "").isalpha():
            raise ValueError("Customer name should contain only alphabets.")

        return True

    @staticmethod
    def validate_amount(amount):
        """
        Validate deposit/withdraw amount.
        """
        if amount <= 0:
            raise InvalidAmountError()

        return True

    @staticmethod
    def validate_pin(pin):
        """
        Validate 4-digit PIN.
        """
        if len(pin) != 4:
            raise ValueError("PIN must contain exactly 4 digits.")

        if not pin.isdigit():
            raise ValueError("PIN should contain only numbers.")

        return True

    @staticmethod
    def validate_account_type(account_type):
        """
        Validate account type.
        """
        valid_types = ["Savings", "Current", "Student"]

        if account_type not in valid_types:
            raise ValueError(
                "Account type must be Savings, Current, or Student."
            )

        return True