class ATM:
	def __init__(self,balance): #private variable
		self.__balance = balance
	def deposit(self,amount): #method
		self.__balance+=amount
		print(f"deposited {amount} . New balance{self.__balance}")
	def withdrawl(self,amount):
		if amount<=self.__balance:
			self.__balance-=amount
			print(f"withdrawl {amount} .new balance {self.__balance}")
		else:
			print("Amount is insufficient")
			
a = ATM(1000)
a.deposit(500)
a.withdrawl(200)