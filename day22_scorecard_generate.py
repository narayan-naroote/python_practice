class StudentData:

    def __init__(self, name, roll_no):

        self.name = name
        self.roll_no = roll_no
        self.__marks = {}

    # Add marks
    def add_marks(self, subject, marks):

        self.__marks[subject] = marks

    # Calculate average
    def avrg_score(self):

        total = 0

        for mark in self.__marks.values():

            total += mark

        avrg = total / len(self.__marks)

        return avrg

    # Calculate grade
    def grade_cal(self):

        average = self.avrg_score()

        if average >= 90:
            return "A"

        elif average >= 80:
            return "B"

        else:
            return "C"

    # Result pass/fail
    def result(self):

        is_passed = all(mark >= 35 for mark in self.__marks.values())

        if is_passed:
            return "Passed"

        else:
            return "Failed"

    # Getter method
    def get_marks(self):

        return self.__marks


class ScoreCard:

    def generate(self, student: StudentData):

        student_marks = student.get_marks()

        print(f"Name : {student.name}")
        print(f"Roll No : {student.roll_no}")

        print("----------- MARKS -----------")

        for subject, mark in student_marks.items():

            print(f"{subject} : {mark}")

        print("-----------------------------")

        print(f"Average : {student.avrg_score():.2f}")
        print(f"Grade : {student.grade_cal()}")
        print(f"Result : {student.result()}")


# Object creation
s1 = StudentData("Narayan", 101)

# Adding marks
s1.add_marks("Maths", 95)
s1.add_marks("Physics", 88)
s1.add_marks("Chemistry", 91)

# Generate scorecard
report = ScoreCard()

report.generate(s1)