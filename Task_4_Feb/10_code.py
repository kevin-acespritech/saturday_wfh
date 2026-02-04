'''10. Find highest salary.
Input:
{'salary':[25000,45000,30000]}
Output:
Highest salary = 45000
'''
data_given  = {'salary':[25000,45000,30000]}
max_salary = 0
obj = data_given['salary']
for value  in obj:  
    
    if value > max_salary:
        max_salary= value
print(f" Higest salary = {max_salary}")