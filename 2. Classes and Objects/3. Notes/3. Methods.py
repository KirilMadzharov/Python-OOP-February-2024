"""
Methods
"""


"Instance Methods"

# Define the behavior of the object

# ▪ The instance object is passed as a first argument of the method
# - using "self" by convention

# class MobilePhone:
#     def __init__(self):
#         self.is_on = True
#
#     def turn_off(self):
#         self.is_on = False
#
#
# phone = MobilePhone()
# print(phone.is_on)  # True
#
# phone.turn_off()
# print(phone.is_on)  # False



"Special/ Dunder Methods"

#  Built-in methods that you can define to add "magic" to your classes
# ▪ Surrounded by double underscores e.g., __init__
# ▪ Enrich the class design and enhance the readability


"We can change the state of the object using methods"

class Dog:
    def __init__(self, name):
        self.name = name
    def change_name(self, new_name):
        self.name = new_name

x = Dog("Max")
x.change_name("Rex")

print(x.name) # Rex