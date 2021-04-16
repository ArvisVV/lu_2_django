class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

    def generate_report(self, average):
        return f'Student {self.name} average grade = {average:.2f}'
