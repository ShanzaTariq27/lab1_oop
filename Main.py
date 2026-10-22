print("Hello VS")
from course import Course, InvalidMarksError, load_course

# Task 2 test
c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)
print(len(c))
print(c.average())
print(c.top_student())

# Task 3 test
try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)
print(c)

# Task 4 test
course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())

# wrong file name test
load_course("Programming for AI", "mark.txt")





#Task1 student cls
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 50

    def __str__(self):
        if self.passed():
            result = "Pass"
        else:
            result = "Fail"
        return f"{self.name} ({self.marks}): {result}"


students = [Student("Ali", 72), Student("Sara", 45), Student("Omar", 50)]

for s in students:
    print(s)