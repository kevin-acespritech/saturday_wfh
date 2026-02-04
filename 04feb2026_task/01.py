'''1. Store student details and display them.
        Input:
        students = [
        {'name':'Aarav','age':20,'marks':85},
        {'name':'Diya','age':22,'marks':90}
        ]
        Output:
        Aarav 20 85
        Diya 22 90'''

students = [
        {'name':'Aarav','age':20,'marks':85},
        {'name':'Diya','age':22,'marks':90}
        ]

for student in students:
    for data in student.values():
        print(data, end=" ")
    print()