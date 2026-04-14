"""
Program: Human Class Example
Description: Demonstrates object creation using constructors and default values in Python (OOP).
Author: Narayan
"""

class Human:
    def __init__(self, name="Unknown", age=0, salary="no salary"):
        """Constructor to initialize Human object"""
        self.name = name
        self.age = age
        self.salary = salary

    def walk(self):
        """Method to display human details"""
        print(f"My name is {self.name}, salary is {self.salary}, and age is {self.age}")


# Creating objects
d = Human("chandan", 34, 45000)
c = Human("darshan",49)
pappu = Human()

# Calling methods
d.walk()
c.walk()
pappu.walk()
