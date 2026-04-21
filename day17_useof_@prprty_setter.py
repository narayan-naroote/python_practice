class Student:
    def __init__(self, phy):
        self.phy = phy

    @property
    def phy(self):
        return self.__phy

    @phy.setter
    def phy(self, value):
        if 0 <= value <= 100:
            self.__phy = value
        else:
            print("Invalid marks")

s1 = Student(90)

# Access (looks same as direct)
print(s1.phy)   # ✅ 90

# Modification (controlled)
s1.phy = 99   
print(s1.phy)