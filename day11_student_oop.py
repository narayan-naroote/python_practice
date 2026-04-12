#creating class name student
class Student: 
    def __init__(self, name): #constrctor func
        self.name = name
#method function
    def display(self): #self:take current obj
        print("Name is:", self.name)


# Creating object
s1 = Student("Narayan")

# Calling method
s1.display()