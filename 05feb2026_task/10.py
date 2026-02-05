'''10. Reverse mapping (value → list of keys).
        Input:
        {"a":[1,2],"b":[2,3]}
        Output:
        {1:["a"],2:["a","b"],3:["b"]}'''

data = {"a":[1,2],"b":[2,3]}
result = {}

for key, values in data.items():
    for value in values:
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)
print(result)