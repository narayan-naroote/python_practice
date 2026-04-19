class Student:
	def __init__(self, name, marks): #Constructor takes parameters
		self.name = name
		self.marks = marks
	def get_avg(self):
		sum = 0
		for val in self.marks: #takes each val from passed list and store it in sum variable
			sum += val
		print("your name is " ,self.name,"and","you are marks  avg is ",round(sum/3,2)) #roundup decimal places
			
s1 = Student("narayan",[99,67,45])
s1.get_avg()