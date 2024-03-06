class Father:
    def __init__(self):
        self.father_name = "Radion"

class Mother:
    def __init__(self):
        self.mother_name = "Tsenka"

class Son(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'

child = Son()

print(child.get_parent_info())