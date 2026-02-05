'''22. Remove duplicate sublists.
        Input:
        [[1,2],[2,1],[1,2]]
        Output:
        [[1,2],[2,1]]
        '''

data = [[1,2],[2,1],[1,2]]
result = []

for value in data:
    if value not in result:
        result.append(value)

print(result)
