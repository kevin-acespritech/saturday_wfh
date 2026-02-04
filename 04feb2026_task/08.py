'''8. Add new employee details.
        Input:
        {'name':['A'],'salary':[20000]}
        Add: B, 30000
        Output:
        {'name':['A','B'],'salary':[20000,30000]}
'''

employees = {'name':['A'],'salary':[20000]}

emp_name = input("enter your name!:")
emp_salary = int(input("enter your salary!:"))

employees['name'].append(emp_name)
employees['salary'].append(emp_salary)
print(employees)