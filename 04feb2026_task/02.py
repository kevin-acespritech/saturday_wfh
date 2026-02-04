'''2. Find student with highest marks.
        Input:
        [{'name':'A','marks':70},{'name':'B','marks':90}]
        Output:
        B has highest marks'''

data = [{'name':'A','marks':70},{'name':'B','marks':90}]
max_marks = 0
temp = None

for dict in data:
    for key in dict:
        if dict['marks'] > max_marks:
            max_marks = dict['marks']
            temp = dict
            
print(f"{temp['name']} has highest marks!")
        