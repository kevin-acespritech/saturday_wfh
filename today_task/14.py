'''14. Class-level vs Instance-level Attributes
       Input: Set `cls.count = 0` and modify inside __init__
       Output: Different values for class and instance'''

class Student:
    marks = 33

    def __init__(self, value):
        self.marks = value

student_1 = Student(56)
student_2 = Student(78)

print(f"Class value : {Student.marks}")
print(f"obj_1 value : {student_1.marks}")
print(f"obj_2 value : {student_2.marks}")

Student.marks = 40
print(f"Class value : {Student.marks}")
print(f"obj_1 value : {student_1.marks}")
print(f"obj_2 value : {student_2.marks}")