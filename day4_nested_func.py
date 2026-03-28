# Nested function
def calculate(a,b):
	def add():
		print(a+b)
	def sub():
		print(a-b)
	def mult():
		print(a*b)
	add()               #inner funtion calls
	sub() 
	mult()
calculate(5,4)      #outer function call
