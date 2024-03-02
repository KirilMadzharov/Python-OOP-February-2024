"""
__repr__() - returns a machine-readable representation of any user defined class
"""

class MyClass:
    def __repr__(self):
        return 'This is My Class'

my_instance = MyClass()

print(repr(my_instance))
print(my_instance.__repr__())
print(my_instance) # This is My Class

# use print() only when __repr__() returns string