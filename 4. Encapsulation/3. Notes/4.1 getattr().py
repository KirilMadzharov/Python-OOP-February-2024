"""

getattr() is a built-in Python function that is used to get the value of an attribute of an object.

It takes three parameters:

The object from which to retrieve the attribute.
The name of the attribute.
An optional default value to return if the attribute does not exist.

Here's the general syntax:
"""

"getattr(object, attribute_name, default_value)"


class Example:
    def __init__(self):
        self.attribute = "Hello, World!"


# Create an instance of the Example class
obj = Example()

# Using getattr() to retrieve the value of the attribute
value = getattr(obj, 'attribute')

print(value)  # Output: Hello, World!
