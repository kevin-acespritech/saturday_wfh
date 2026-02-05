'''7. Replace missing keys with 0.
        Input:
        [{"a":1},{"b":2}]
        Output:
        [{"a":1,"b":0},{"a":0,"b":2}]
        '''

data = [{"a":1},{"b":2}]
keys = set().union(*data)

for dict in data:
    for key in keys:
        dict.setdefault(key, 0)
print(data)