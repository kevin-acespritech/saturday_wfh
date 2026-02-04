'''7. Find average salary.
Input:
{'salary':[30000,40000,50000]}
Output:
Average salary = 40000
'''
data = {'salary':[30000,40000,50000]}
sum = 0
for  value in (data['salary']):
    sum+=value
print(f"Average salary is {sum // len(data['salary'])}")
