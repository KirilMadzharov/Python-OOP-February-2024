"""
Data Attributes
"""

# ▪ Values that are stored internally and are unique to that object
# ▪ They define the state of the object
#
# ▪ There are two types of data attributes:
# ▪ Instance variables
# ▪ Class variables

"Instance vs Class Variables"


# Instance variables are unique to each instance
# Class variables are shared by all instances of the class

# class Laptop:
#     brand = "Dell" # class variable
#
#     def __init__(self, name):
#         self.name = name # instance variable
#
# first_laptop = Laptop("Latitude 5300")
# second_laptop = Laptop("Inspiron 15")
#
# print(first_laptop.brand == second_laptop.brand) # True
# print(first_laptop.name == second_laptop.name) # False


# It is not a good practice to declare or remove data attributes outside the class

# Good Practice:

class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name
        self.tricks = []  # creates empty list for each dog


poodle = Dog("Bella")
beagle = Dog("Max")

print(poodle.name, poodle.kind)  # Bella canine
print(beagle.name, beagle.kind)  # Max canine

poodle.tricks.append('roll over')
beagle.tricks.append('play dead')

print(poodle.tricks)  # ['roll over']
print(beagle.tricks)  # ['play dead']
