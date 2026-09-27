class BankAccount:
    def __init__(self):
       self.balance = 0

    def add_money(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def apply_interest(self):
        self.balance += self.balance * 0.05

    def transfer(self, target_account,amount):
        self.withdraw(amount)
        target_account.add_money(amount)

