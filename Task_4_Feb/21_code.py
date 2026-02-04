'''21. Find average marks using list of dict.
Input:
{'marks':[80,90,100]}
Output:
Average = 90
'''


given_data = {'marks':[80,90,100]}


total = 0
obj  = given_data['marks']
for value in obj:
    total = total + value
    avg_ans= total// len(obj)


print(f"Average = {avg_ans}")