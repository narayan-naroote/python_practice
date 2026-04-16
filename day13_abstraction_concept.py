# Abstraction Concept in Python

# Importing required modules
from abc import ABC, abstractmethod


# Abstract class (Blueprint)
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        """
        Abstract method that must be implemented
        by all child classes
        """
        pass


# Child class implementing abstraction
class Car(Vehicle):

    def start(self):
        # Hidden internal logic
        print("Checking fuel...")
        print("Turning ignition...")
        print("Engine started")


# Creating object
car = Car()

# Calling method
car.start()