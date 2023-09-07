
class Student:
    def __init__(self, name, student_id, english, math, science):
        self.name = name
        self.student_id = student_id
        self.english = english
        self.math = math
        self.science = science

    def get_name(self):
        return self

    def get_student_id(self):
        return self.student_id

    def get_english(self):
        return self.english

    def get_math(self):
        return self.math

    def get_science(self):
        return self.science

    def get_total(self):
        return self.english + self.math + self.science

    def get_average(self):
        return round(self.get_total() / 3, 1)

    def __str__(self):
        return "Name: {}, ID: {}\nEnglish quiz score: {}, Mathematics quiz score: {}\nScience quiz score: {}, Total: {}, Average: {}".format(self.name, self.student_id, self.english, self.math, self.science, self.get_total(), self.get_average())


name = input("Enter the student's name: ")
id = input("Enter the student's ID: ")
english = int(input("Enter the student's English quiz score: "))
math = int(input("Enter the student's mathematics quiz score: "))
science = int(input("Enter the student's science quiz score: "))

s = Student(name, id, english, math, science)
print(s)