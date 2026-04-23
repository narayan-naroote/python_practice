#overloading in python

class calc:
	def add(self, a,b,c=0): #default overloading
		return a+b+c
		
s1 = calc()
print(s1.add(1,2,5))
print(s1.add(1,5))