"""
=========================================================
SecureBank Console Application
File: services/account_service.py
Description: Business Logic Layer
=========================================================
"""

from models.account import Account
from utils.validator import Validator
from exceptions.custom_exceptions import (
    AccountNotFoundError,
    InvalidAmountError,
    InsufficientFundsError,
    InvalidPINError,
    AccountClosedError
)


class AccountService:

    def __init__(self):
        self.accounts = {}
        self.account_counter = 100001

    def generate_account_number(self):
        account_number = f"SB{self.account_counter}"
        self.account_counter += 1
        return account_number

    def create_account(self, name, account_type, pin, balance):

        Validator.validate_name(name)
        Validator.validate_account_type(account_type)
        Validator.validate_pin(pin)
        Validator.validate_amount(balance)

        account_number = self.generate_account_number()

        account = Account(
            account_number=account_number,
            customer_name=name,
            account_type=account_type,
            pin=pin,
            balance=balance
        )

        account.add_transaction(
            f"Account Created with Opening Balance ₹{balance}"
        )

        self.accounts[account_number] = account

        print("\n===================================")
        print("   Account Created Successfully")
        print("===================================")
        print("Account Number :", account_number)
        print("Customer Name  :", name)
        print("Account Type   :", account_type)
        print("Opening Balance: ₹", balance)
        print("===================================")

        return account_number

    def get_account(self, account_number):

        if account_number not in self.accounts:
            raise AccountNotFoundError()

        account = self.accounts[account_number]

        if account.status == "CLOSED":
            raise AccountClosedError()

        return account

    def deposit(self, account_number, amount):

        Validator.validate_amount(amount)

        account = self.get_account(account_number)

        account.deposit(amount)

        print("\n===================================")
        print("      Deposit Successful")
        print("===================================")
        print("Account Number :", account.account_number)
        print("Deposited      : ₹", amount)
        print("Current Balance: ₹", account.balance)
        print("===================================")

    def withdraw(self, account_number, pin, amount):

        Validator.validate_amount(amount)

        account = self.get_account(account_number)

        if account.pin != pin:
            raise InvalidPINError()

        if amount > account.balance:
            raise InsufficientFundsError()

        account.withdraw(amount)

        print("\n===================================")
        print("     Withdrawal Successful")
        print("===================================")
        print("Withdrawn      : ₹", amount)
        print("Current Balance: ₹", account.balance)
        print("===================================")

    def check_balance(self, account_number):

        account = self.get_account(account_number)

        print("\n===================================")
        print("        ACCOUNT BALANCE")
        print("===================================")
        print("Customer :", account.customer_name)
        print("Balance  : ₹", account.balance)
        print("===================================")

        return account.balance

    def close_account(self, account_number, pin):

        account = self.get_account(account_number)

        if account.pin != pin:
            raise InvalidPINError()

        account.close_account()

        print("\n===================================")
        print(" Account Closed Successfully")
        print("===================================")
        print("Account :", account.account_number)
        print("Status  :", account.status)
        print("===================================")

    def search_account(self, account_number):

        account = self.get_account(account_number)

        account.display()

        return account

    def mini_statement(self, account_number):

        account = self.get_account(account_number)

        account.mini_statement()

    def bank_statistics(self):

        total_accounts = len(self.accounts)
        active_accounts = 0
        closed_accounts = 0
        total_balance = 0
        highest_balance = 0
        richest_customer = "N/A"

        for account in self.accounts.values():

            total_balance += account.balance

            if account.status == "ACTIVE":
                active_accounts += 1
            else:
                closed_accounts += 1

            if account.balance > highest_balance:
                highest_balance = account.balance
                richest_customer = account.customer_name

        print("\n===================================")
        print("        BANK STATISTICS")
        print("===================================")
        print("Total Accounts   :", total_accounts)
        print("Active Accounts  :", active_accounts)
        print("Closed Accounts  :", closed_accounts)
        print("Total Balance    : ₹", total_balance)
        print("Highest Balance  : ₹", highest_balance)
        print("Richest Customer :", richest_customer)
        print("===================================")