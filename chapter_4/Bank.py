from Account import *


class Bank():
    def __init__(self) -> None:
        self.accounts_dict = {}
        self.next_account_number = 0

    def ask_for_valid_account_number(self):
        account_number = input("What is your account number? ")
        try:
            account_number = int(account_number)
        except ValueError:
            raise AbortTransaction("The account number must be an integer")
        if account_number not in self.accounts_dict:
            raise AbortTransaction(
                f"There is no account {str(account_number)}")
        return account_number

    def ask_for_valid_password(self, account):
        password = input("What is your password? ")
        account.check_password(password)

    def get_account(self):
        account_number = self.ask_for_valid_account_number()
        account = self.accounts_dict[account_number]
        self.ask_for_valid_password(account)
        return account

    def create_account(self, name, starting_balance, password):
        new_account = Account(name, password, starting_balance)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = new_account
        self.next_account_number += 1
        return new_account_number

    def open_account(self):
        print("*** Open Account ***")
        user_name = input("What is the name for the new user account? ")
        starting_balance = input(
            "What is the stating balance for this account? ")
        password = input(
            "What is the password you want to user for this account? ")
        user_account_number = self.create_account(
            user_name, starting_balance, password)
        print("Your new account number is:", user_account_number)
        print()

    def close_account(self):
        print("*** Close Account ***")
        account = self.get_account()
        balance = account.get_balance()
        if balance:
            print("You had", balance,
                  "in your account, which is being returned to you.")
        self.accounts_dict.pop(account)
        print("Your account is now closed")

    def balance(self):
        print("*** Get Balance ***")
        account = self.get_account()
        balance = account.get_balance()
        if balance is not None:
            print("Your balance is: ", balance)

    def deposit(self):
        print("*** Deposit ***")
        account = self.get_account()
        amount = input("Please enter the amount to deposit: ")
        balance = account.deposit(amount)
        if balance is not None:
            print("Your new balance is:", balance)

    def show(self):
        print("*** Show ***")
        for account_number in self.accounts_dict:
            account = self.accounts_dict[account_number]
            print("Account number: ", account_number)
            account.show()

    def withdraw(self):
        print("*** Withdraw ***")
        account = self.get_account()
        amount = input("Please enter the amount to withdraw: ")
        balance = account.withdraw(amount)
        if balance is not None:
            print("Your new balance is:", balance)

    def bank_info(self):
        print("Hours: 9 to 5")
        print("Address: 123 Main Street, Anytown, USA")
        print("Phone: (650) 555-1212")
        print("We currently have", len(self.accounts_dict), "account(s) open.")
