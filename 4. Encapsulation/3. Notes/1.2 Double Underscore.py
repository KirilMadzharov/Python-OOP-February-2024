"""
When naming an attribute with two leading underscores, it
invokes name mangling

▪ In Python, mangling is used for attributes that one class
does not want subclasses to use
▪ Python does not restrict access to such attributes
▪ It is still possible to access or modify a variable that is
considered "private" from outside the class
"""


class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self):
        print(f"I am {self.name}, {self.__age} years old.")

    # Getter method for the age
    def get_age(self):
        return self.__age


person = Person('Peter', 25)

# Accessing data using the class method
person.info()  # I am Peter, 25 years old.

# Accessing data directly from outside
print(person.name)  # Peter

# Accessing private attribute age via a public method
print(person.get_age())  # 25
