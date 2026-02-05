'''15. Replace list with its average.
        Input:
        {"a":[2,4],"b":[1,3,5]}
        Output:
        {"a":3,"b":3}
        '''

data = {"a":[2,4],"b":[1,3,5]}

for key, values in data.items():
    data[key] = [(sum(values)) // len(values)]

print(data)