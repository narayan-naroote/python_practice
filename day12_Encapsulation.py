# Encapsulation Concept in Python

class BankAccount:
    def __init__(self, balance):
        # Private variable (cannot be accessed directly)
        self.__balance = balance

    def deposit(self, amount):
        # Method to add money to the account
        self.__balance += amount

    def get_balance(self):
        # Method to access private data
        return self.__balance


# Creating object
acc = BankAccount(5000)

# Depositing amount
acc.deposit(1000)

# Displaying updated balance
print("Updated Balance:", acc.get_balance())