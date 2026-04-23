#flexible arguments 
class Calc:
    def add(self, *args):
        return sum(args)

a1 = Calc()

print(a1.add(1, 2))            # 3
print(a1.add(1, 2, 3, 4))      # 10