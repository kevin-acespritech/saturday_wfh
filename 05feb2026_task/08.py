'''8. Find dictionary with maximum unique values.
        Input:
        [{"a":1,"b":1},{"a":1,"b":2}]
        Output:
        {"a":1,"b":2}
        '''

data = [{"a":1,"b":1},{"a":1,"b":2}]
max_uniqe = 0
result = None


for dict in data:
    values = set(dict.values())
    if len(values) > max_uniqe:
        result = dict
    
print(result)