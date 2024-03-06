""""
Hierarchical inheritance occurs when more than one derived class is created from a single base class.

This means that siblings (derived classes) share a common parent (base class) but are otherwise
independent of each other, each potentially adding its own attributes and methods.

Here's a simple example to illustrate hierarchical inheritance in Python:
"""

# Base class
class Parent:
    def __init__(self):
        self.parent_name = "Parent"

    def show_parent(self):
        print("Parent Name:", self.parent_name)


# Derived class 1
class Daughter(Parent):
    def __init__(self):
        super().__init__()  # Initialize the base class constructor
        self.daughter_name = "Daughter"

    def show_daughter(self):
        print("Daughter Name:", self.daughter_name)


# Derived class 2
class Son(Parent):
    def __init__(self):
        super().__init__()  # Initialize the base class constructor
        self.son_name = "Son"

    def show_son(self):
        print("Son Name:", self.son_name)


# Creating objects of the derived classes
daughter = Daughter()
son = Son()

# Calling methods
daughter.show_parent()
daughter.show_daughter()

son.show_parent()
son.show_son()

