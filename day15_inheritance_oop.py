class Car:
    color = "Blue"

    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped...")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


class Fortuner(ToyotaCar):
    def __init__(self, name, fuel_type):
        super().__init__(name)
        self.fuel_type = fuel_type


c1 = Fortuner("Fortuner", "Diesel")

print(c1.name)
print(c1.fuel_type)
print(c1.color)

c1.start()
