"""
Name mangling is a technique used in Python to make attributes or methods of a class more "private" by
 adding a prefix of double underscores to their names. This is primarily done to avoid accidental overriding
 of these attributes or methods by subclasses.

To perform name mangling on a method in Python, you can prefix the method name with double underscores.

Here's an example:
"""


class MyClass:
    def __init__(self):
        self.__private_method()

    def __private_method(self):
        print("This is a private method")


my_object = MyClass()
# Trying to access the private method from outside the class will raise an AttributeError
# my_object.__private_method()


"""
In this example, __private_method() is a private method that can only be accessed within the MyClass class. 

If you try to access it from outside the class, you'll get an AttributeError. 

However, it's worth noting that Python doesn't have true access control mechanisms like some other languages do. 

Name mangling provides a convention rather than true privacy, and it's still possible to access these attributes
or methods with a bit of workaround.
"""