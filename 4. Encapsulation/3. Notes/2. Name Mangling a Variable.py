"""
Name Mangling a Variable
"""


# ▪ Used to show that the variable should not be accessed
# outside the class

class Car:
    def __init__(self):
        self.__max_speed = 200

    def drive(self):
        print('driving max speed ' + str(self.__max_speed))


red_car = Car()
red_car.drive()  # driving max speed 200
red_car.__max_speed = 10  # won't change the __max_speed attribute because it is private


