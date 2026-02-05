'''27. Deep merge dictionaries with sum.
        Input:
        {"a":{"x":1}}, {"a":{"x":4,"y":2}}
        Output:
        {"a":{"x":5,"y":2}}
        '''
def deep_merge(d1, d2):
    result = {}

    for key in d1.keys() | d2.keys():
        if key in d1 and key in d2:
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                result[key] = deep_merge(d1[key], d2[key])
            else:
                result[key] = d1[key] + d2[key]
        else:
            result[key] = d1.get(key, d2.get(key))

    return result

d1 = {"a":{"x":1}}
d2 = {"a":{"x":4,"y":2}}
answer = deep_merge(d1, d2)
print(answer)