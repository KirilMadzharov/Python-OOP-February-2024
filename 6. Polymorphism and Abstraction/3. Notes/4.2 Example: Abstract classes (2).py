class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError("Subclasses must implement abstract method")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Bark!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print("Meow!")


cat = Cat("Willy")
cat.sound()  # Meow!
dog = Dog("Willy")
dog.sound()  # Bark!

try:
    animal = Animal("Willy")
    animal.sound()  # This will raise a NotImplementedError
except NotImplementedError as e:
    print("Error!")  # This will catch the exception and print "Error!"
