'''21. Find average marks using list of dict.
            Input:
            {'marks':[80,90,100]}
            Output:
            Average = 90'''

data = {'marks':[80,90,100]}
sum = 0
for marks in data['marks']:
    sum += marks

print(f"average = {sum // len(data['marks'])}")