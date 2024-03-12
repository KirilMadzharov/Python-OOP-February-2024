"""
Getter and Setter Methods
"""


# Used to access and change the private variables as they are
# part of the class

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name)
        print(self.__age)

    def get_age(self):  # getter
        print(self.__age)

    def set_age(self, age):  # setter
        self.__age = age


person = Person('Peter', 25)
# Accessing data using class method
person.info()  # Outputs: Peter 25
# Changing age using setter
person.set_age(26)
person.get_age()  # Outputs: 26
