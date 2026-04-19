class Account:

    def __init__(self, balance, accountno):
        self.balance = balance
        self.accountno = accountno

    def debit(self, amount):
        self.balance -= amount
        print("Amount debited:", amount,)
        print("Total amount:", self.show_balance())

    def credit(self, amount):
        self.balance += amount
        print("Amount credited:", amount)
        print("Total amount:", self.show_balance())

    def show_balance(self):
        return self.balance

    def show_details(self):
        print("Account No:", self.accountno)
        print("Balance:", self.balance)


# Creating object
acc = Account(1000, 123456)

# Using methods
acc.credit(200)
acc.debit(150)
acc.show_balance()
acc.show_details()
