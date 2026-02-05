'''25. Swap outer and inner keys.
        Input:
        {"x":{"a":1},"y":{"a":2}}
        Output:
        {"a":{"x":1,"y":2}}'''

data = {"x":{"a":1},"y":{"a":2}}
result = {}

output_dict = {}

for outer_key, inner_dict in data.items():
    for inner_key, value in inner_dict.items():
        if inner_key not in result:
            result[inner_key] = {}
        result[inner_key][outer_key] = value

print(result)