'''26. Remove inner keys with zero values.
        Input:
        {"a":{"x":0,"y":2},"b":{"x":1,"y":0}}
        Output:
        {"a":{"y":2},"b":{"x":1}}'''

data = {"a":{"x":0,"y":2},"b":{"x":1,"y":0}}

for outer_key, inner_dict in data.items():
    keys_to_remove = []
    for inner_key, value in inner_dict.items():
        if value == 0:
            keys_to_remove.append(inner_key)
            
    for key in keys_to_remove:
        del inner_dict[key]
        
print(data)

