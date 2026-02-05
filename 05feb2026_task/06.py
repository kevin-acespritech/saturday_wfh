'''6. Sort list of dicts by sum of values.
        Input:
        [{"a":1,"b":2},{"a":5},{"a":2,"b":1}]
        Output:
        [{"a":1,"b":2},{"a":2,"b":1},{"a":5}]
        '''

data = [{"a":1,"b":2},{"a":5},{"a":2,"b":1}]

result = sorted(data, key = lambda x: sum(x.values()))

print(result)