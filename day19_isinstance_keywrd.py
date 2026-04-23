class Student:
	def __init__(self, name, age):
		self.__name = name
		self.__age = age
		
	def get_name(self):
		return self.__name
		
	def set_name(self, name):
			self.__name = name
	def set_age(self,age):
			if isinstance(age, int):
				self.age = age
			else:
				print("Age should be integer. ERROR!")
			
student = Student("Amit", 34)
student.set_age("wvshsh") #age should be integer.ERROR!