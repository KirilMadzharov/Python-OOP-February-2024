# The following example is NOT A GOOD PRACTICE:

class Shape:
    def __init__(self):
        if type(self) is Shape:
            raise Exception('This is an abstract class')


def area(self):
    raise Exception('This is an abstract class')


def perimeter(self):
    raise Exception('This is an abstract class')


"""
Abstract Classes with ABC Module
"""

# Abstract base classes (ABCs) enforce derived classes to implement particular methods from the base class
# ▪ We implement it using the abcmodule


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius
