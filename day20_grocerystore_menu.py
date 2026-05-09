def display_menu():
    print("\n===== Grocery Store Menu =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Cart & Total Price")
    print("4. Exit")


cart = []

while True:
    display_menu()

    choice = int(input("Enter your choice: "))

    # Add Item
    if choice == 1:

        name = input("Enter product name: ")
        price = int(input("Enter product price: "))

        cart.append((name, price))

        print(f"{name} added to cart successfully!")

    # Remove Item
    elif choice == 2:

        name = input("Enter product name to remove: ")

        found = False

        for item in cart:

            if item[0] == name:

                cart.remove(item)
                found = True

                print(f"{name} removed from cart!")
                break

        if not found:
            print("Item not found in cart.")

    # View Cart and Total Price
    elif choice == 3:

        if len(cart) == 0:
            print("Cart is empty.")

        else:

            print("\nItems in Cart:")

            total = 0

            for name, price in cart:

                print(f"{name} --> ₹{price}")
                total += price

            print("----------------------")
            print("Total Price:", total)

    # Exit
    elif choice == 4:

        print("Thank you for shopping with us!")
        break

    # Invalid Choice
    else:

        print("Invalid choice! Please enter between 1 to 4.")