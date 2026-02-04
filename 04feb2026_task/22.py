'''22. Convert dictionary of lists to list of dicts.
        Input:
        {'name':['A','B'],'age':[20,22]}
        Output:
        [{'name':'A','age':20},{'name':'B','age':22}]
        '''

data = {'name':['A','B'],'age':[20,22]}
result = []

for i in range(len(data['name'])):
    temp = {}
    for key, value in data.items():
        temp.update({key:value[i]})

    result.append(temp)
print(result)
