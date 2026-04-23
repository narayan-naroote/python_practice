class Student:
    def __init__(self, name, age):
        self.__name = name #private
        self.__age = age

    def get_age(self):  #getter method 
        return self.__age

    def set_age(self, age): #setter method 
        if age > 0:
            self.__age = age  
        else:
            print("Invalid age")

student = Student("mohan", 22)

# Accessing age with getter
print("Age :", student.get_age())

# Updating age with setter
student.set_age(20)

# Printing updated age
print("Updated Age :", student.get_age())