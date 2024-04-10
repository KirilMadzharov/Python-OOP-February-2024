"""
Abstraction
"""

"""
Abstraction in Python, as in other programming languages, is a fundamental concept in object-oriented programming (OOP)
that helps in hiding the complex implementation details of a program and showing only the necessary features of an
object to the outside world. 

This process of hiding the real implementation of an application from the user and  emphasizing only on usage of it is 
known as abstraction. 

In Python, abstraction can be achieved using abstract classes and interfaces.

Abstract Classes

An abstract class is a class that cannot be instantiated on its own and is designed to be subclassed. 

It can contain one or more abstract methods. An abstract method is a method that is declared in the abstract class, 
but it must be implemented by the subclass. 

The abc module in Python provides the infrastructure for defining custom abstract base classes.

To create an abstract class in Python, you follow these steps:

Import the ABC (Abstract Base Class) and abstractmethod decorator from the abc module.
Define your class and make it inherit from ABC.
Decorate one or more methods with the @abstractmethod decorator to make them abstract methods.

Here's a simple example to demonstrate:
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


"""
In this example, Shape is an abstract class because it has abstract methods area and perimeter. The Rectangle class 
inherits from Shape and implements the abstract methods, providing the specific implementation details for calculating 
the area and perimeter of a rectangle.

Interfaces

While Python does not have explicit support for interfaces as seen in languages like Java, the concept is similarly 
used in the form of enforcing certain methods to be implemented by a class. Abstract classes in Python serve a similar 
purpose to interfaces, dictating a set of methods that must be implemented by any non-abstract subclass.

Abstraction allows for more flexible and maintainable code, enabling different implementations to be swapped easily as 
long as they adhere to the same interface defined by an abstract class. This encapsulation of complexity is a 
key principle in designing robust and scalable software systems.
"""
