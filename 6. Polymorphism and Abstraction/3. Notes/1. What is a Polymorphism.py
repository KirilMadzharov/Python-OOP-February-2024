"""
Polymorphism is a concept in Python (and other object-oriented programming languages) that refers to
the ability of different types of objects to be accessed through the same interface, with each type responding
in its own way to the same method call. In simpler terms, it means that the same function or method can work in
 different ways depending on the object it is called on.

Here’s a straightforward example to illustrate this:

Imagine you have a bunch of different animal toys, and each of them can make a sound. Even though the
action is the same ("make a sound"), each animal toy does it differently: a dog might "bark," a cat might
 "meow," and a cow might "moo."

In Python, polymorphism lets us define a method in the base (or parent) class and then have each subclass
implement the method in a way that's specific to it. This way, when we call the method on an object without
knowing or caring about its specific class, the correct version of the method is invoked, and the appropriate
 action is taken based on the actual class of the object.

Here's a quick example in code to make it clear:
"""


class Animal:
    def make_sound(self):
        pass  # This is just a placeholder to be overridden by subclasses


class Dog(Animal):
    def make_sound(self):
        return "Bark"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


# Use polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())

"""
In this example, both Dog and Cat are animals, and they both 'make sound,' but the sound they make is different.
When we iterate through the animals list and call make_sound() on each animal, polymorphism ensures that the correct 
method is called for each specific animal object, producing the appropriate sound for each type of animal.
"""
