'''11. Store marks and calculate total.
Input:
[['Anu',80,90],['Raj',70,75]]
Output:
Anu total = 170
Raj total = 145'''

students = []
user_total = int(input("enter total student : "))

for data in range(user_total):
    stu_name = input("Enter name: ")
    score_1 = int(input("Enter first marks: "))
    score_2 = int(input("Enter second marks: "))
    students.append([stu_name ,score_1 ,score_2])

for student in students:
    stu_name = student[0]
    total = student[1] + student[2]

    print(f"{stu_name} total = {total}")