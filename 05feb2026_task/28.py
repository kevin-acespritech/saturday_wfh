'''28. Count total inner keys.
        Input:
        {"a":{"x":1,"y":2},"b":{"z":3}}
        Output:
        3'''

data = {"a":{"x":1,"y":2},"b":{"z":3}}
count = 0

for inner_dict in data.values():
    if isinstance(inner_dict, dict):
        count += len(inner_dict)
    
print(count)
