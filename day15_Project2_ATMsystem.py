from abc import ABC, abstractmethod

# 🔹 Abstraction (Rule class)
class ATM(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


# 🔹 Encapsulation + Implementation
class MyBankATM(ATM):

    def __init__(self, balance, pin):
        self.__balance = balance   # private variable
        self.__pin = pin           # private PIN

    def verify_pin(self, pin):
        return pin == self.__pin

    def withdraw(self, amount):
        pin = int(input("Enter PIN: "))
        if self.verify_pin(pin):
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdraw successful")
            else:
                print("Insufficient balance")
        else:
            print("Wrong PIN")

    def deposit(self, amount):
        pin = int(input("Enter PIN: "))
        if self.verify_pin(pin):
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Wrong PIN")

    def check_balance(self):
        pin = int(input("Enter PIN: "))
        if self.verify_pin(pin):
            print("Balance:", self.__balance)
        else:
            print("Wrong PIN")


# 🔹 Main Program
atm = MyBankATM(1000, 1234)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = int(input("Enter amount: "))
        atm.deposit(amt)

    elif choice == 2:
        amt = int(input("Enter amount: "))
        atm.withdraw(amt)

    elif choice == 3:
        atm.check_balance()

    elif choice == 4:
        print("\nThank you!\n Wisit again...!")
        break

    else:
        print("Invalid choice")