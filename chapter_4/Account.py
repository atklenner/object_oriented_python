class Account():
    def __init__(self, name, password, balance) -> None:
        self.name = name
        self.password = password
        self.balance = int(balance)

    def deposit(self, password, amount):
        if password != self.password:
            print("Incorrect password")
            return None
        
        if amount < 0:
            print("You cannot deposit a negative amount")
            return None

        self.balance += int(amount)
        return self.balance

    def withdraw(self, password, amount):
        if password != self.password:
            print("Incorrect password")
            return None

        if amount < 0:
            print("You cannot withdraw a negative amount")
            return None

        self.balance -= amount
        return self.balance

    def get_balance(self, password):
        if password != self.password:
            print("Incorrect password")
            return None

        return self.balance

    def show(self):
        print("name:", self.name)
        print("password", self.password)
        print("balance", self.balance)
