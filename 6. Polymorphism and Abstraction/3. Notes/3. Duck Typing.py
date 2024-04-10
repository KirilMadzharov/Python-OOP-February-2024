"""
Duck typing
"""

"""
"Duck typing" in Python refers to a style of dynamic typing where an object's suitability for use in a specific context
 is determined by the presence of certain methods and properties, rather than the actual type of the object itself.

This concept is summed up by the phrase: "If it looks like a duck, swims like a duck, and quacks like a duck, 
then it probably is a duck."

In the context of programming, this means that an object's compatibility with an operation doesn't depend on its 
class inheritance or the explicit implementation of an interface, but rather on the presence of certain methods or 
attributes. 

Python, being a dynamically typed language, employs duck typing extensively, allowing for more flexible and 
intuitive code design.

For example, you can iterate over items in any object that implements the __iter__ method or supports the sequence
 protocol (__getitem__ and __len__ methods), whether it's a list, tuple, string, file, or any custom class that meets
this criterion. 

Here's a simple demonstration of duck typing:
"""

class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(duck):
    duck.quack()

duck = Duck()
person = Person()

# Both `duck` and `person` can be used with `make_it_quack` because they both have a `quack` method.
make_it_quack(duck)  # Outputs: Quack, quack!
make_it_quack(person)  # Outputs: I'm quacking like a duck!


# This approach emphasizes operations and behaviors rather than the strict type of the object, encouraging more
# flexible and generic code design.

