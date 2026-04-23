#Type-based overloading 
class Calc:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c

a1 = Calc()

print(a1.add(2, 3))       # 5
print(a1.add(2, 3, 4))    # 9