"""
Multilevel inheritance in Python involves a chain of classes where a class is derived from another derived class,
forming a "grandparent-parent-child" relationship.

This allows the child class to inherit attributes and methods from the parent class, which in turn
inherits from the grandparent class.

Here's a simple example to illustrate this concept:
"""


# Grandparent class
class Grandparent:
    def __init__(self):
        self.grandparent_name = "Grandparent"

    def show_grandparent(self):
        print("Grandparent Name :", self.grandparent_name)


# Parent class inheriting Grandparent class
class Parent(Grandparent):
    def __init__(self):
        super().__init__()  # Initialize grandparent's __init__ method
        self.parent_name = "Parent"

    def show_parent(self):
        print("Parent Name :", self.parent_name)


# Child class inheriting Parent class
class Child(Parent):
    def __init__(self):
        super().__init__()  # Initialize parent's __init__ method
        self.child_name = "Child"

    def show_child(self):
        print("Child Name :", self.child_name)


# Creating an object of the Child class
child = Child()

# Calling methods
child.show_grandparent()
child.show_parent()
child.show_child()
