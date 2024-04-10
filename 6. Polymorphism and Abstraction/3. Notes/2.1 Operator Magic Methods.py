"""
Operator Magic Methods
"""

"""
In Python, magic methods (also known as dunder methods, short for "double underscore") are special methods that start 
and end with double underscores. They enable operator overloading and allow custom classes to implement behavior that 
mimics that of Python's built-in types. Here's a brief overview of the magic methods you've mentioned and the operators
 they are associated with:

1. `__add__(self, other)`: This method is called when the addition operator (`+`) is used. It allows objects of your 
class to be added together or to other objects if you define appropriate logic.

2. `__sub__(self, other)`: This method is invoked when the subtraction operator (`-`) is used. It allows objects of
 your class to be subtracted from each other or from other objects.

3. `__mul__(self, other)`: This method is called with the multiplication operator (`*`). It enables objects of your 
class to be multiplied by each other or by other objects.

4. `__floordiv__(self, other)`: This method is associated with the floor division operator (`//`). It allows objects 
of your class to perform floor division with each other or with other objects.

5. `__truediv__(self, other)`: This method is called when the true division operator (`/`) is used. It lets objects 
of your class perform division that always produces a floating point result.

6. `__pow__(self, other[, modulo])`: This method corresponds to the exponentiation operator (`**`). It enables objects
 of your class to be raised to the power of other objects. Optionally, a modulo can be applied to the result if specified.

These magic methods allow you to define how your objects should behave with common operators, giving you the flexibility
 to implement custom behavior for mathematical or other operations.
"""


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        else:
            return Number(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        else:
            return Number(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)
        else:
            return Number(self.value * other)

    def __floordiv__(self, other):
        if isinstance(other, Number):
            return Number(self.value // other.value)
        else:
            return Number(self.value // other)

    def __truediv__(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value)
        else:
            return Number(self.value / other)

    def __pow__(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value)
        else:
            return Number(self.value ** other)

    def __repr__(self):
        return f"Number({self.value})"


# Addition
a = Number(10)
b = Number(20)
print(a + b)  # Number(30)
print(a + 5)  # Number(15)

# Subtraction
print(a - b)  # Number(-10)
print(b - 5)  # Number(15)

# Multiplication
print(a * b)  # Number(200)
print(a * 2)  # Number(20)

# Floor Division
print(b // a)  # Number(2)
print(b // 3)  # Number(6)

# True Division
print(a / b)  # Number(0.5)
print(b / 2)  # Number(10.0)

# Exponentiation
print(a ** b)  # Number(10**20)
print(a ** 3)  # Number(1000)
