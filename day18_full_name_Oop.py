#Parent class
class Family:
	def __init__(self, surname):
		self.surname = surname

#Child class inherit from parent class	
class child(Family):
	def __init__(self,surname,name):
		super().__init__(surname) #inherit
		self.name = name
f1 = child("naroote", "narayan") #object creation

print(f" Full Name:{f1.name}.{f1.surname}")