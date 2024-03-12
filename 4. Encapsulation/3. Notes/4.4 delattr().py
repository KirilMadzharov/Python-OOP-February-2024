"""
delattr() is a built-in Python function used to delete the specified attribute from an object.


It takes two parameters:

The object from which to delete the attribute.
The name of the attribute to delete.


Here's the general syntax:
"""


#  delattr(object, attribute_name)


class Example:
    def __init__(self):
        self.attribute = "Hello, World!"


# Create an instance of the Example class
obj = Example()

# Using delattr() to delete the attribute
delattr(obj, 'attribute')

# Trying to access the attribute after deletion will raise an AttributeError
print(obj.attribute)  # This line will raise an AttributeError
