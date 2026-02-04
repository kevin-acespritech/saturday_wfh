'''6. Store employee data and display row-wise.
Input:
{'name':['Rohit','Sneha'],'salary':[50000,60000]}
Output:
Rohit 50000
Sneha 60000
'''
data  = {'name':['Rohit','Sneha'],'salary':[50000,60000]}

for row in zip(*data.values()):
    print(row[0], row[1])
