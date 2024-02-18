"""
Building Data Functionality Together
"""

# What is an Object-Oriented Programming?
#
#  It is the most popular programming paradigm
#
# ▪ It relies on the concept of classes and objects
# ▪ A class is used to create an individual instance of an object


"Advantages of OOP"

# ▪ Provides a clear program structure, and a clean code
# ▪ Reduces complexity
# ▪ Make it easy to write a reusable code
# ▪ Could test each behavior of an object separately
# ▪ Facilitates easy maintenance and modification of existing code


"Objects in Python"

# Everything in Python is an object and has a type

# ▪ 10.5
# ▪ "Python"
# ▪ [1, 2, 3, 4]
# ▪ {"name": "Peter", "age": 26}

# ▪ We could create as many objects as we like, manipulate them, or remove them


"What is an Object?"

# Object is a data abstraction that captures an internal representation and an interface

# ▪ The internal representation should be private
# ▪ The interface defines behaviors but hides implementation


"Characteristics of an Object"

#  State
#
# ▪ Help to distinguish an object from other objects
# ▪ A phone could have a color, a size, a weight
#
# ▪ Behavior
#
# ▪ The tasks that an object performs
# ▪ A phone could turn on, turn off


"What is a Class?"


# The class is a blueprint that defines the nature of a future object
# ▪ In Python, a class is created by the keyword class

class Phone:
    # State:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    # Behaviour:
    def turn_on(self):
        return 'The phone is turned on'


"What is an Instance?"


#  Specific realization of an object of a certain class
# ▪ The creation of an instance is called instantiation

class Phone:
    # State:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    # Behaviour:
    def turn_on(self):
        return 'The phone is turned on'

#Instance:
phone = Phone("blue", 4.7)



"Creating and Using Classes"

# The keyword class defines a new type

class Person:
    pass

# We define the state of the object using attributes

class Person:

    #special method __innit__
    def __init__(self, name, age):

        #Atributes:
        self.name = name
        self.age = age



"Method"

# ▪ We define the behavior of the object using methods
# ▪ It is like a function, that works only within a class

