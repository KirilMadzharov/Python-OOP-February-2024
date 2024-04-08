"""
Class Methods
"""

#  It is bound to the class and not the object of
# the class
# ▪ It can modify a class state that would apply
# across all the instances of the class
# ▪ To turn a method into a class method, we add a
# line with @classmethod in front of the
# method header


"Example: Class Methods"


# We generally use class method to create factory methods

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def pepperoni(cls):
        return cls(["tomato sauce", "parmesan", "pepperoni"])

    @classmethod
    def quattro_formaggi(cls):
        return cls(["mozzarella", "gorgonzola", "fontina", "parmigiano"])


first_pizza = Pizza.pepperoni()
second_pizza = Pizza.quattro_formaggi()


"Benefits"

# ▪ Simply provide a shortcut for creating new
# instance objects
# ▪ Ensures correct instance creation of the
# derived class
# ▪ You could easily follow the Don't Repeat Yourself
# (DRY) principle using class methods
