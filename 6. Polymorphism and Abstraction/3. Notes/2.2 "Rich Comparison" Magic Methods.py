"""
"Rich Comparison" Magic Methods
"""

"""
In Python, "magic methods" (also known as "dunder" methods, for "double underscore") are special methods with fixed 
names that provide implementations for built-in behavior. The "rich comparison" magic methods allow objects of custom 
classes to use comparison operators (<, <=, ==, !=, >, >=). Each method corresponds to a specific operator:

__lt__(self, other) for less-than (<)
__le__(self, other) for less-than-or-equal-to (<=)
__eq__(self, other) for equal-to (==)
__ne__(self, other) for not-equal-to (!=)
__gt__(self, other) for greater-than (>)
__ge__(self, other) for greater-than-or-equal-to (>=)
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    # Less than: <
    def __lt__(self, other):
        return self.area() < other.area()

    # Less than or equal: <=
    def __le__(self, other):
        return self.area() <= other.area()

    # Equal: ==
    def __eq__(self, other):
        return self.area() == other.area()

    # Not equal: !=
    def __ne__(self, other):
        return self.area() != other.area()

    # Greater than: >
    def __gt__(self, other):
        return self.area() > other.area()

    # Greater than or equal: >=
    def __ge__(self, other):
        return self.area() >= other.area()


# Create two rectangles
rect1 = Rectangle(5, 10)  # Area = 50
rect2 = Rectangle(7, 8)  # Area = 56

# Compare them
print(rect1 < rect2)  # True, because 50 is less than 56
print(rect1 <= rect2)  # True
print(rect1 == rect2)  # False
print(rect1 != rect2)  # True
print(rect1 > rect2)  # False
print(rect1 >= rect2)  # False
