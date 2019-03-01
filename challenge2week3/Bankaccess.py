class BankAccount:
    def __init__(self):
        self.open = False
        self.initial_balance = 0

    def get_balance(self):
        if not self.open:
            raise ValueError("Transactions cannot be made: Reason, account closed")
        return self.initial_balance

    def open(self):
        self.is_open = True

    def deposit(self, amount):
        if not self.open:
            raise ValueError("Transactions cannot be made: Reason, account closed")
        if amount < 0:
            raise ValueError("Money cannot be negative")

        self.initial_balance += amount
        return self.initial_balance

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError( "Transactions cannot be made: Reason, account closed")
        if amount < 0:
            raise ValueError("Money cannot be negative")
        if amount > self.get_balance():
            raise ValueError("Money cannot be negative")
        self.initial_balance -= amount
        return self.initial_balance

    def close(self):
        self.open = False
