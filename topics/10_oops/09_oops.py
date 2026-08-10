
from numpy import real

class Complex:
    def __init__(self, real, imag):
            self.real = real
            self.imag = imag

    def showNumber(self):
        print(self.real, "+", self.imag, "i")

    def add(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)

num1 = Complex(2, 3)
num1.showNumber()  # Output: 2 + 3 i

num2 = Complex(4, 5)
num2.showNumber()  # Output: 4 + 5 i

num3 = num1.add(num2)
num3.showNumber()  # Output: 6 + 8 i

# Method 2:

class Complex:
    def __init__(self, real, imag):
            self.real = real
            self.imag = imag

    def showNumber(self):
        print(self.real, "+", self.imag, "i")

    def __add__(self, num2): # This method is called when we use the + operator between two Complex objects. Here, Dunder method __add__ is used to overload the + operator for Complex class. It takes another Complex object as an argument and returns a new Complex object which is the sum of the two Complex numbers.
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)

num1 = Complex(2, 3)
num1.showNumber()  # Output: 2 + 3 i

num2 = Complex(4, 5)
num2.showNumber()  # Output: 4 + 5 i

num3 = num1 + num2
num3.showNumber()  # Output: 6 + 8 i

# Subtraction using Dunder method __sub__:
class Complex:
    def __init__(self, real, imag):
            self.real = real
            self.imag = imag

    def showNumber(self):
        print(self.real, "+", self.imag, "i")

    def __add__(self, num2): # This method is called when we use the + operator between two Complex objects. Here, Dunder method __add__ is used to overload the + operator for Complex class. It takes another Complex object as an argument and returns a new Complex object which is the sum of the two Complex numbers.
            newReal = self.real + num2.real
            newImag = self.imag + num2.imag
            return Complex(newReal, newImag)

    def __sub__(self, num2): # This method is called when we use the - operator between two Complex objects. Here, Dunder method __sub__ is used to overload the - operator for Complex class. It takes another Complex object as an argument and returns a new Complex object which is the difference of the two Complex numbers.
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal, newImag)

num1 = Complex(2, 3)
num1.showNumber()  # Output: 2 + 3 i

num2 = Complex(4, 5)
num2.showNumber()  # Output: 4 + 5 i

num3 = num1 - num2
num3.showNumber()  # Output: -2 + -2 i


# Other than lecture-------------------------------

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# Uses:
c1 = Complex(2, 3)
c2 = Complex(1, 4)

print(c1 + c2)  # Output: 3 + 7i
print(c1 - c2)  # Output: 1 + -1i
print(c1 * c2)  # Output: -10 + 11i
print(c1 / c2)  # Output: 0.8235294117647058 + -0.29411764705882354i

