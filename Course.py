class InvalidMarksError(Exception):
    pass


class Course:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_student(self, student, marks):
        if not 0 <= marks <= 100:
            raise InvalidMarksError(f"Invalid marks for {student}: {marks}")
        self.marks[student] = marks

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        return max(self.marks, key=self.marks.get)

    def __len__(self):
        return len(self.marks)

    def __str__(self):
        return f"{self.name}: {len(self)} students, average {self.average():.1f}"


def load_course(name, filename):
    course = Course(name)
    try:
        with open(filename) as f:
            for line in f:
                student, mark = line.strip().split(",")
                try:
                    course.add_student(student, int(mark))
                except ValueError:
                    print(f"Skipping {student}: marks is not a number")
                except InvalidMarksError as e:
                    print(f"Skipping: {e}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return course

#task 5
if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)