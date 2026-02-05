'''23. Flatten nested dictionary.
        Input:
        {"a":{"x":1},"b":{"y":2}}
        Output:
        {"a.x":1,"b.y":2}
        '''

data = {"a":{"x":1},"b":{"y":2}}
result = {}

def flatten_dict(data, parent_key = ''):
    for key, value in data.items():
        new_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            flatten_dict(value, new_key)
        else:
            result[new_key] = value
    return result

answer = flatten_dict(data)
print(answer)