# Personal Account Management

## About the Project

This is a simple Python project where I created a personal bank account system using OOP

The program allows a user to:
- Deposit money
- Withdraw money
- Check the current balance
- See transaction history

goal of this assignment was to practice working with:
- Classes
- Objects
- Lists of objects
- Encapsulation
- Operator overloading

---

## Classes Used

### Amount
This class represents a single transaction

Each transaction has:
- amount
- date and time
- type (DEPOSIT or WITHDRAWAL)

---

### PersonalAccount
This class represents bank account

It stores:
- account number
- account holder name
- current balance
- list of transactions

Main features:
- deposit money
- withdraw money (with balance check)
- print transaction history
- check balance
- use + and - operators to deposit/withdraw

---

## How It Works

When money is deposited or withdrawn:
1. A new `Amount` object is created.
2. It is added to the transaction list.
3. The account balance is updated.

One PersonalAccount contains many Amount objects

---

## How to Run

1. Make sure Python 3 is installed.
2. Open terminal in the project folder.
3. Run: **python personal_account.py**

---

## Test Cases

program was tested for:
- Depositing valid amount
- Withdrawing valid amount
- Trying to withdraw more than available balance
- Checking balance after multiple transactions
- Printing transaction history when empty and when filled

---

## Author

Islambek Asylbekov