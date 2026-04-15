#TYPES of Constructor
#defaul constructor
class Test:
	def __init__(self):
		print("This is a default constructor")
t=Test()

#Parameterized Constructor
class Test:
	def __init__(self , x):
		self.x = x
t = Test("10")
print(t.x)