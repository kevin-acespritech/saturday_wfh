'''3. Remove dictionaries where all values are zero.
        Input:
        [{"a":0,"b":0},{"a":1,"b":0},{"a":0,"b":2}]
        Output:
        [{"a":1,"b":0},{"a":0,"b":2}]
        '''

data = [{"a":0,"b":0},{"a":1,"b":0},{"a":0,"b":2}]

for dict in data:
    for value in dict.values():
        if value != 0:
            break
    else:
        data.remove(dict)
        
print(data)