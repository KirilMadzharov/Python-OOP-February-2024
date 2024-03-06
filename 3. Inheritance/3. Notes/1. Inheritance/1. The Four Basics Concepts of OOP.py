"""
The Four Basic Concepts of OOP
"""

"Inheritance"

# Extend the functionality of the code's existing classes to eliminate repetitive code

"Encapsulation"

# Stop objects from interacting with each other so classes cannot change or interact with the specific variables and
# functions of an object

"Abstraction"

# Isolate the impact of changes made to the code so the change will only affect the variables shown and not the
# outside code

"Polymorphism"


# Allows different classes to have methods with the same name


# Example of Inheritance

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(Person):
    pass


student = Student("Kiril", "Madzharov")

print(student.first_name)
print(student.last_name)
print(student.get_full_name())
