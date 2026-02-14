from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = float(amount)
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.timestamp} | {self.transaction_type} | ${self.amount:.2f}"


class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []


    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += amount
        print(f"Deposited ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        transaction = Amount(amount, "WITHDRAWAL")
        self.transactions.append(transaction)
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}")

    def print_transaction_history(self):
        if not self.transactions:
            print("No transactions found.")
            return

        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    #string representation
    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: ${self.balance:.2f}")

    #operator overloading
    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self


#sample test
if __name__ == "__main__":
    account = PersonalAccount(12345, "Islam Asylbekov")

    account.deposit(500)
    account.withdraw(150)

    print("\nCurrent Balance:", account.get_balance())

    account.print_transaction_history()

    # Using overloaded operators
    account + 200
    account - 100

    print("\nFinal Account Info:")
    print(account)
