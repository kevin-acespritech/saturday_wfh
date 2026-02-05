'''5. Convert list of dicts to dict of lists.
        Input:
        [{"name":"A","score":90},{"name":"B","score":80}]
        Output:
        {"name":["A","B"],"score":[90,80]}'''

data = [{"name":"A","score":90},{"name":"B","score":80}]
result = {}

for dict in data:
    for key, value in dict.items():
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    
print(result)