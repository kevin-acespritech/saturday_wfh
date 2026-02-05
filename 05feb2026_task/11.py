'''11. Remove keys whose list sum < 5.
        Input:
        {"a":[1,2],"b":[10],"c":[2,2]}
        Output:
        {"b":[10]}
        '''

data = {"a":[1,2],"b":[10],"c":[2,2]}
result = {}

for key, values in data.items():
    if sum(values) > 5:
        result.update({key:values})
print(result)