class Students:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    def percentage(self):
        return round((self.phy + self.chem + self.math) / 3, 2)

s1 = Students(89, 67, 56)

print("Old %:", s1.percentage())

# 🔹 Change marks
s1.math = 99

print("New %:", s1.percentage())