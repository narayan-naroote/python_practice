print("----WELcome to My Calculator----")
while True:
    choice = input("Enter operation (+, -, *, /, //) or AC to exit: ").upper()
    
    if choice == 'AC':
        print("Calculator cleared/stopped")
        break
    
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    if choice == '+':
        print(f"Result: {a + b}")
    elif choice == '-':
        print(f"Result: {a - b}")
    elif choice == '*':
        print(f"Result: {a * b}")
    elif choice == '/':
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Cannot divide by zero")
    elif choice == '//':
        print(f"Result: {a // b}")
    else:
        print("Invalid choice")