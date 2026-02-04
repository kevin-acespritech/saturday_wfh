'''8. Add new employee details.
Input:
{'name':['A'],'salary':[20000]}
Add: B, 30000
Output:
{'name':['A','B'],'salary':[20000,30000]}
'''

employees_detail = {'name':['A'],'salary':[20000]}

name_input=  input("Enter your name: ")

salary_input = int(input("Enter your salary: "))

employees_detail['name'].append(name_input)
employees_detail['salary'].append(salary_input)

print(employees_detail)