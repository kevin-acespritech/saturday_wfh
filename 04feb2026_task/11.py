'''11. Store marks and calculate total.
        Input:
        [['Anu',80,90],['Raj',70,75]]
        Output:
        Anu total = 170
        Raj total = 145'''

students = [['Anu',80,90],['Raj',70,75]]

for student in students:
    total = 0
    for marks in student:
        if isinstance(marks, int):
            total += marks
    
    print(f"{student[0]} total = {total}")