'''
    2. Find student with highest marks.
    Input:
    [{'name':'A','marks':70},{'name':'B','marks':90}]
    Output:
    B has highest marks'''

sample_data = [{'name':'A','marks':70},{'name':'B','marks':90}]

students = [
    {'name': 'A', 'marks': 70},
    {'name': 'B', 'marks': 90}
]

max_marks = students[0]

for obj in students:
    if obj['marks'] > max_marks['marks']:
        max_marks = obj

print(f"{max_marks['name']} has highest marks")
