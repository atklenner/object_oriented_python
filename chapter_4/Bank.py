from Account import *

class Bank():
    def __init__(self) -> None:
        self.accounts_dict = {}
        self.next_account_number = 0

    def create_account(self, name, starting_balance, password):
        new_account = Account(name, password, starting_balance)
        new_account_number = self.next_account_number
        self.accounts_dict[new_account_number] = new_account
        self.next_account_number += 1
        return new_account_number

    def open_account(self):
        print("*** Open Account ***")
        user_name = input("What is the name for the new user account? ")
        starting_balance = input("What is the stating balance for this account? ")
        starting_balance = int(starting_balance)
        password = input("What is the password you want to user for this account? ")
        user_account_number = self.create_account(user_name, starting_balance, password)
        print("Your new account number is:", user_account_number)
        print()

    def close_account(self):
        print("*** Close Account ***")
        account_number = input("What is your account number? ")
        account_number = int(account_number)
        password = input("What is your password? ")
        account = self.accounts_dict[account_number]
        balance = account.get_balance(password)
        if balance:
            print("You had", balance, "in your account, which is being returned to you.")
        del self.accounts_dict[account_number]
        print("Your account is now closed")

    def balance(self):
        print("*** Get Balance ***")
        account_number = input("Please enter your account number: ")
        account_number = int(account_number)
        password = input("Please enter the password: ")
        account = self.accounts_dict[account_number]
        balance = account.get_balance(password)
        if balance is not None:
            print("Your balance is: ", balance)

    def deposit(self):
        print("*** Deposit ***")
        account_number = input("Please enter your account number: ")
        account_number = int(account_number)
        amount = input("Please enter the amount to deposit: ")
        amount = int(amount)
        password = input("Please enter the password: ")
        account = self.accounts_dict[account_number]
        balance = account.deposit(password, amount)
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
        account_number = input("Please enter your account number: ")
        account_number = int(account_number)
        amount = input("Please enter the amount to withdraw: ")
        amount = int(amount)
        password = input("Please enter the password: ")
        account = self.accounts_dict[account_number]
        balance = account.withdraw(password, amount)
        if balance is not None:
            print("Your new balance is:", balance)

    def bank_info(self):
        print("Hours: 9 to 5")
        print("Address: 123 Main Street, Anytown, USA")
        print("Phone: (650) 555-1212")
        print("We currently have", len(self.accounts_dict), "account(s) open.")