class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def status(self):
        return self.size - self.quantity

    def fill(self, liters):
        if (self.quantity + liters) > self.size:
            pass
        else:
            self.quantity += liters


# Test Code

cup = Cup(100, 50)

print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
