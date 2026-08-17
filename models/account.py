"""
=========================================================
SecureBank Console Application
File: models/account.py
Description: Account Model using Python Dataclass
=========================================================
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Account:
    """
    Represents a bank account in the SecureBank system.
    """

    account_number: str
    customer_name: str
    account_type: str
    pin: str
    balance: float = 0.0
    status: str = "ACTIVE"

    created_at: str = field(
        default_factory=lambda: datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    )

    transactions: list = field(default_factory=list)

    def deposit(self, amount):
        """
        Deposit money into account.
        """
        self.balance += amount

        self.transactions.append(
            f"[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] "
            f"Deposit : ₹{amount}"
        )

    def withdraw(self, amount):
        """
        Withdraw money from account.
        """
        self.balance -= amount

        self.transactions.append(
            f"[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] "
            f"Withdraw : ₹{amount}"
        )

    def add_transaction(self, message):
        """
        Add custom transaction.
        """
        self.transactions.append(
            f"[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] {message}"
        )

    def display(self):
        """
        Display account information.
        """
        print("\n======================================")
        print("         ACCOUNT DETAILS")
        print("======================================")
        print(f"Account Number : {self.account_number}")
        print(f"Customer Name  : {self.customer_name}")
        print(f"Account Type   : {self.account_type}")
        print(f"Balance        : ₹{self.balance:.2f}")
        print(f"Status         : {self.status}")
        print(f"Created On     : {self.created_at}")
        print("======================================")

    def mini_statement(self):
        """
        Display transaction history.
        """
        print("\n======================================")
        print("          MINI STATEMENT")
        print("======================================")

        if len(self.transactions) == 0:
            print("No transactions found.")
        else:
            for transaction in self.transactions:
                print(transaction)

        print("--------------------------------------")
        print(f"Available Balance : ₹{self.balance:.2f}")
        print("======================================")

    def close_account(self):
        """
        Close account.
        """
        self.status = "CLOSED"

        self.transactions.append(
            f"[{datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')}] "
            "Account Closed"
        )