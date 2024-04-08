"""
In Python, method overriding allows a subclass to provide a specific implementation of a method that is already defined
 in its superclass. Overriding is commonly done with instance methods, where a subclass provides its own implementation
 of a method with the same name and signature as in the superclass.

However, Python also allows overriding using class methods. Class methods are methods that are bound to the class rather
 than its instances. They receive the class itself as the first argument (usually named cls conventionally) instead of
 an instance of the class. To override a class method in Python, you can define a class method with the same name in the
  subclass as in the superclass.

Here's an example demonstrating how to override a class method in Python:
"""


class Parent:
    @classmethod
    def class_method(cls):
        print("Parent class method")


class Child(Parent):
    @classmethod
    def class_method(cls):
        print("Child class method")


# Test the overridden class method
Child.class_method()  # Output: Child class method
