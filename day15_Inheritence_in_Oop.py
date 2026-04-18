# Inheritance Concept in Object-Oriented Programming (OOP)

# 🔹 Parent Class (Base Class)
class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} has logged in")


# 🔹 Child Class (Derived Class)
class Admin(User):  # Inheriting from User
    def delete_user(self):
        print(f"{self.username} deleted a user")


# 🔹 Creating objects
user = User("narayan")
user.login()

admin = Admin("admin_narayan")
admin.login()          # Inherited method
admin.delete_user()    # Child class method