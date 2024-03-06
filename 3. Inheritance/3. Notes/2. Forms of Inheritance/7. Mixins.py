""""
Mixins are a type of multiple inheritance in Python where a class is designed to provide
 a certain functionality to be inherited by other classes, without being intended for
  standalone use. Mixins allow for the sharing of methods across multiple classes.

  Here's an example to illustrate how mixins can be used in Python to add functionality
  to classes:

Imagine we have a system where we want to add logging and JSON serialization capabilities
to our classes without cluttering their core functionalities.

We can create mixins for both these functionalities.
"""

class LoggerMixin:
    """Mixin class that adds logging functionality."""
    def log(self, message: str):
        print(f"Log message: {message}")

class JsonMixin:
    """Mixin class that adds JSON serialization functionality."""
    def to_json(self):
        import json
        # Assumes that the class using this mixin has a method or property `to_dict` that returns its information as a dictionary.
        return json.dumps(self.to_dict())

# Example class using the mixins
class Vehicle(LoggerMixin, JsonMixin):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def to_dict(self):
        """Convert the Vehicle instance data to a dictionary."""
        return {"make": self.make, "model": self.model}

# Creating an instance of Vehicle
car = Vehicle("Tesla", "Model S")

# Utilizing mixin methods
car.log("Vehicle instance created.")
print(car.to_json())
