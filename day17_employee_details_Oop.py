class Employees:
	def __init__(self, role, dept, salary):
		self.role = role
		self.dept = dept
		self.salary = salary
	def showDetails(self):
		print("Role : ",self.role)
		print("Dept : ",self.dept)
		print("Salary : ",self.salary)
e1 = Employees("Accountant", "Finance", "60,000")
print(e1.showDetails())