"""
__str__() - returns a printable string representation of any user defined class
"""


class MyClass:
    def __str__(self):
        return 'This is My Class'


my_instance = MyClass()

print(str(my_instance))  # This is My Class
print(my_instance.__str__())  # This is My Class
print(my_instance)  # This is My Class
