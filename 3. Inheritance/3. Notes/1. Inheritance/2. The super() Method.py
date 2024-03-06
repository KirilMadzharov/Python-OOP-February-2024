class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def __init__(self, first_name, last_name, student_number):
        # Person.__init__(self, last_name) - it is the same with the super() method
        super().__init__(first_name, last_name)
        self.student_number = student_number

    def get_id(self):
        return self.student_number

student = Student("Kiril", "Madzharov", 1234)

print(student.first_name)
print(student.last_name)
print(student.student_number)
print(student.get_id())

