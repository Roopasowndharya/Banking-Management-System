"""
=========================================================
SecureBank Console Application
Main File: bank_console.py
=========================================================
"""

from services.account_service import AccountService


def display_menu():
    print("\n" + "=" * 50)
    print("🏦        SECURE BANK MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Search Account")
    print("6. Mini Statement")
    print("7. Bank Statistics")
    print("8. Close Account")
    print("9. Exit")
    print("=" * 50)


def main():

    service = AccountService()

    while True:

        display_menu()

        choice = input("Enter your choice (1-9): ")

        try:

            if choice == "1":

                print("\n------ Create Account ------")

                name = input("Customer Name : ")
                account_type = input("Account Type (Savings/Current/Student): ")
                pin = input("Create 4 Digit PIN : ")
                balance = float(input("Opening Balance : "))

                service.create_account(
                    name,
                    account_type,
                    pin,
                    balance
                )

            elif choice == "2":

                print("\n------ Deposit ------")

                account = input("Account Number : ")
                amount = float(input("Amount : "))

                service.deposit(account, amount)

            elif choice == "3":

                print("\n------ Withdraw ------")

                account = input("Account Number : ")
                pin = input("PIN : ")
                amount = float(input("Amount : "))

                service.withdraw(account, pin, amount)

            elif choice == "4":

                account = input("Account Number : ")

                service.check_balance(account)

            elif choice == "5":

                account = input("Account Number : ")

                service.search_account(account)

            elif choice == "6":

                account = input("Account Number : ")

                service.mini_statement(account)

            elif choice == "7":

                service.bank_statistics()

            elif choice == "8":

                account = input("Account Number : ")
                pin = input("PIN : ")

                service.close_account(account, pin)

            elif choice == "9":

                print("\nThank you for using SecureBank.")
                print("Good Bye 👋")
                break

            else:

                print("Invalid Choice.")

        except Exception as error:

            print("\nError :", error)


if __name__ == "__main__":
    main()