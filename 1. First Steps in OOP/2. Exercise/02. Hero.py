class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"


    def heal(self, amount):
        self.health += amount


# Test code

hero = Hero("Peter", 100)
print(hero.defend(50))  # Output will be None, which means nothing is printed
hero.heal(50)
print(hero.defend(99))  # Output will be None, which means nothing is printed
print(hero.defend(1))  # Output will be "Peter was defeated"
