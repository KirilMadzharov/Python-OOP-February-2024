"Class Objects"


# Classes support two kinds of operations:
#
# attribute references - access them using the "." operator
# instantiation - uses function notations

# Examples:

# class ExampleClass: # we do not use snake case for class names - we use "PascalCase"
#     text = "Hello"
#
#     def print_text(self):
#         return "SoftUni"
#
#
# ExampleClass.text # attribute reference
# ExampleClass.print_text()  # attribute reference
# x = ExampleClass # instantiation


class Car:  # Definition class
    car_tank_capacity = 90

    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        return "Engine starts"


car1 = Car("Diesel")  # Crete object class
car2 = Car("Petrol")  # Instance class

car1.engine = "Hybrid"

print(car1.engine)  # Hybrid
print(car2.engine)  # Petrol

car1.car_tank_capacity = 100

print(car1.car_tank_capacity)  # 100
print(car2.car_tank_capacity)  # 90

print(car1.start_engine())  # Engine starts



"Instantiation"


# It is known as "calling" the class
# ▪ Creates an empty object - new instance of the class
# ▪ Assigns the object to a local variable

class Person:
    name = "George"
    age = 25


person = Person()
print(person.name)  # George
print(person.age)  # 25



"__init__()"

# Creates objects with instances, customized to a specific initial state
# ▪ Automatically invoked for the newly created class instance

# class instance
class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model

my_laptop = Laptop("Inspiron 15", "Dell")



"self Parameter"

# self is used to represent the instance of the class
# ▪ It binds the attributes with the given arguments
# ▪ It is not a keyword, but using it increases the readability of code

class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model

my_laptop = Laptop("Inspiron 15", "Dell")



"Instance Objects"

# Instances support only one kind of operation:
# ▪ attribute references - access them using the "." operator


class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model

my_laptop = Laptop("Inspiron 15", "Dell")

print(my_laptop.name) # Inspiron 15
print(my_laptop.model) # Dell

