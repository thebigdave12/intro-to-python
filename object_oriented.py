student = {"name": "Rolf", "grades": (89, 90, 83, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["grades"]))


class Student:
    def __init__(self) -> None: #could do (self, name, grades) next line self.name = name next line self.grades = grades
        self.name = "rolf"
        self.grades = (89, 90, 83, 90)

    def average(self):
        return sum(self.grades) / len (self.grades)


student = Student()

print(student.name)
print(student.grades)
# print(Student.average(student)) 
print(student.average())