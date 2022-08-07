class AbortTransaction(Exception):
    """Raise this exception to abort a bank transaction"""
    pass


class Account():
    def __init__(self, name, password, balance) -> None:
        self.name = name
        self.password = password
        self.balance = self.validate_amount(balance)

    def validate_amount(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            raise AbortTransaction("Amount must be an integer")
        if amount <= 0:
            raise AbortTransaction("Amount must be positive")
        return amount

    def check_password(self, password):
        if password != self.password:
            raise AbortTransaction("Incorrect password")

    def deposit(self, amount):
        amount = self.validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        amount = self.validate_amount(amount)
        if amount > self.balance:
            raise AbortTransaction(
                "You cannot withdraw more than what you have in your account")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def show(self):
        print("name:", self.name)
        print("password", self.password)
        print("balance", self.balance)
