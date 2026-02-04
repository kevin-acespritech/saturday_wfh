'''15. Find student with highest total.
Input:
[['A',50,50],['B',60,70]]
Output:
B'''

data = [['A',50,50],['B',60,70]]
highest = 0
for student in data:
    total = 0
    for mark in student:
        if isinstance(mark , int):
            total +=mark
    if total > highest:
        highest = total
        name= student[0]

print(f"{name}")