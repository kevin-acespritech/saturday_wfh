'''30. Convert dict of dict to list of tuples.
        Input:
        {"a":{"x":1},"b":{"y":2}}
        Output:
        [("a","x",1),("b","y",2)]'''

data = {"a":{"x":1},"b":{"y":2}}
result = []

for outer_key, inner_dict in data.items():
    for key, value in inner_dict.items():
        result.append((outer_key, key, value))
print(result)