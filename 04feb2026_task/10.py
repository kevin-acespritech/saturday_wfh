'''10. Find highest salary.
        Input:
        {'salary':[25000,45000,30000]}
        Output:
        Highest salary = 45000
'''

data = {'salary':[25000,45000,30000]}

data['salary'].sort()
print(f"Highest Salary = {data['salary'][-1]}")