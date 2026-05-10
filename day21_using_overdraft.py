class BankAccount:

    def __init__(self, balance, name, account_no):

        self.__balance = balance
        self.name = name
        self.account_no = account_no

    def display_balance(self):

        print(f"Balance : {self.__balance}")

    def withdraw(self, amount):

        if self.__balance >= amount:

            self.__balance -= amount

            print("Withdrawal successful!")
            print(f"Updated Balance : {self.__balance}")

        else:
            print("Insufficient balance")

    def deposit(self, amount):

        self.__balance += amount

        print("Deposit successful!")
        print(f"Updated Balance : {self.__balance}")

    def get_balance(self):

        return self.__balance


class SavingAccount(BankAccount):

    Interest = 0.05

    def show_interest(self):

        interest_amount = self.get_balance() * self.Interest

        print(f"Interest Added : {interest_amount}")


class CurrentAccount(BankAccount):

    Overdraft = 1000

    # Method Overriding (Polymorphism)
    def withdraw(self, amount):

        if self.get_balance() + self.Overdraft >= amount:

            remaining = self.get_balance() - amount

            print("Withdrawal successful using overdraft!")
            print(f"Remaining Balance : {remaining}")

        else:
            print("Overdraft limit exceeded")


# Object Creation

s1 = CurrentAccount(4000, "Narayan", 4578)

s1.withdraw(5000)