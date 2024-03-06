"""

Method Resolution Order (MRO) in Python 3 is determined by the C3 linearisation algorithm.

It defines the order in which base classes are searched when executing a method.

First, it looks in the child class for the method being called. If the method isn't found, Python then searches
the parent classes one by one in the order they are specified, moving from left to right and then up the hierarchy.

This ensures that if multiple inherited classes have the same method, the first one found in the MRO list is executed.

Here's an example that demonstrates MRO in Python 3:
"""

class A:
    def who_am_i(self):
        print("I am A")

class B(A):
    def who_am_i(self):
        print("I am B")

class C(A):
    def who_am_i(self):
        print("I am C")

class D(B, C):
    pass

# Create an instance of D
d_instance = D()
d_instance.who_am_i()
# This will print "I am B" because of the MRO

print(D.mro())
# This will show you the order in which methods are resolved
