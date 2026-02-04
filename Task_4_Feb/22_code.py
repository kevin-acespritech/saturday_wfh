'''
22. Convert dictionary of lists to list of dicts.
Input:
{'name':['A','B'],'age':[20,22]}
Output:
[{'name':'A','age':20},{'name':'B','age':22}]'''

data = {'name': ['A', 'B'], 'age': [20, 22]}

answer  = []
for i in range(len(data['name'])):
    data_dict = {}
    for key in data:
        data_dict[key] = data[key][i]
    answer.append(data_dict)

print(answer)
