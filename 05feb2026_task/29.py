'''29. Find common inner keys.
        Input:
        {"a":{"x":1,"y":2},"b":{"x":5}}
        Output:
        ["x"]'''

data = {"a":{"x":1,"y":2},"b":{"x":5}}
keys = []
result = set()

for outer_key, inner_dict in data.items():
    keys.extend(list(inner_dict.keys()))

for key in keys:
    if keys.count(key) > 1:
        result.add(key)

print(list(result))
