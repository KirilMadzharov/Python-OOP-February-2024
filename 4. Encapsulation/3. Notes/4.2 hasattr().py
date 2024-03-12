"""
hasattr() is another built-in Python function that is used to check if an object has a given attribute.

It takes two parameters:

The object to check.
The name of the attribute to check for.

Here's the general syntax:
"""


# hasattr(object, attribute_name)

class Example:
    def __init__(self):
        self.attribute = "Hello, World!"


# Create an instance of the Example class
obj = Example()

# Check if the object has the attribute 'attribute'
if hasattr(obj, 'attribute'):
    print("The attribute 'attribute' exists.")
else:
    print("The attribute 'attribute' does not exist.")
