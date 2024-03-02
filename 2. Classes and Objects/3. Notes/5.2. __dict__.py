"""
The __dict__ Attribute
"""


# This is a dictionary containing a module's symbol table

class MyClass:
    class_variable = 1

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


# Create instances of MyClass
first = MyClass(2)
second = MyClass(3)

# Print the __dict__ attribute of the MyClass class
print(MyClass.__dict__)  # This will print the dictionary containing class level attributes

# Print the __dict__ attribute of the instances
print(first.__dict__)  # This will print {'instance_variable': 2}
print(second.__dict__)  # This will print {'instance_variable': 3}
