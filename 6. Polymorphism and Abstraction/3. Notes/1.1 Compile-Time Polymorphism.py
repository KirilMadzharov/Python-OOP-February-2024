"""
Compile-Time Polymorphism
"""


# Python does not support compile-time polymorphism or method overloading

# ▪ If a class has multiple methods with the same name, the method defined in the last will override the earlier one

class Person:
    def say_hello():
        return "Hi!"

    def say_hello():
        return "Hello"


print(Person.say_hello())  # This will print "Hello"
