"""

setattr() is a built-in Python function used to set the value of a specified attribute of an object.

It takes three parameters:

The object on which to set the attribute.
The name of the attribute to set.
The value to assign to the attribute.


Here's the general syntax:
"""


# setattr(object, attribute_name, value)


class Example:
    def __init__(self):
        self.attribute = None


# Create an instance of the Example class
obj = Example()

# Using setattr() to set the value of the attribute
setattr(obj, 'attribute', 'Hello, World!')

# Now let's print the value of the attribute
print(obj.attribute)  # Output: Hello, World!
