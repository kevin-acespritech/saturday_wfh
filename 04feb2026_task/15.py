'''15. Find student with highest total.
        Input:
        [['A',50,50],['B',60,70]]
        Output:
        B'''

data = [['A',50,50],['B',60,70]]
highest_total = 0

for student in data:
    total = 0
    for marks in student:
        if isinstance(marks, int):
            total += marks

    if total > highest_total:
        highest_total = total
        name = student[0]

print(f"{name} has maximum total marks")