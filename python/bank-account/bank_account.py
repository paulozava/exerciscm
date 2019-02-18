class BankAccount(object):
    def __init__(self):
        self.balance = None

    def get_balance(self):
        if self.balance != None:
            return self.balance
        else:
            raise ValueError("Account hasn't balance")

    def open(self):
        if self.balance == None:
            self.balance = 0
        else:
            raise ValueError("Account is already opened")

    def deposit(self, amount):
        if self.balance != None and amount > 0:
            self.balance += abs(amount)
        else:
            raise ValueError("Impossible to deposit")

    def withdraw(self, amount):
        if self.balance != None and amount > 0 and self.balance >= amount:
            self.balance -= abs(amount)
        else:
            raise ValueError("Impossible to deposit")

    def close(self):
        if self.balance != None:
            self.balance = None
        else:
            raise ValueError("Account is already closed")