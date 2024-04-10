from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius  # Private attribute

    def calculate_area(self):
        return 3.141592653589793 * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.141592653589793 * self.__radius


class Rectangle(Shape):

    def __init__(self, height, width):
        self.__height = height  # Private attribute
        self.__width = width  # Private attribute

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


# Test Code

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
