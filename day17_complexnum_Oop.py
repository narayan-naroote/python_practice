# complex_number.py
# Demonstrates a simple Complex Number class using OOP concepts

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def show_number(self):
        """Display the complex number in proper format"""
        print(f"{self.real} + {self.imag}i")

    def add(self, other):
        """Add two complex numbers and return a new Complex object"""
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return Complex(new_real, new_imag)


# 🔹 Example usage
if __name__ == "__main__":
    num1 = Complex(4, 3)
    num2 = Complex(3, 2)

    print("First Number:")
    num1.show_number()

    print("Second Number:")
    num2.show_number()

    print("---------")

    num3 = num1.add(num2)

    print("After Addition:")
    num3.show_number()