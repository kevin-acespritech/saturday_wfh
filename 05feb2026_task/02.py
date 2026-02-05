'''2. Remove duplicate dictionaries ignoring key order.
        Input:
        [{"a":1,"b":2},{"b":2,"a":1},{"a":2,"b":3}]
        Output:
        [{"a":1,"b":2},{"a":2,"b":3}]
        '''

data = [{"a":1,"b":2},{"b":2,"a":1},{"a":2,"b":3}]
result = []

for dict in data:
    if dict in result:
        continue
    else:
        result.append(dict)

print(result)