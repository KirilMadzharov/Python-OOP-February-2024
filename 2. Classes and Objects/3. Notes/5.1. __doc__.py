"""
The __doc__ Attribute
"""


# Provides documentation of the object as a string

class MyClass:
    """This is MyClass."""

    def example(self):
        """This is the example module of MyClass."""


print(MyClass.__doc__)  # This is MyClass.
print(MyClass.example.__doc__)  # This is the example module of MyClass.
