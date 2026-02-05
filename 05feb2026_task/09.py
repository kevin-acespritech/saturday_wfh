'''9. Remove duplicates from each list.
        Input:
        {"a":[1,2,2],"b":[3,3,4]}
        Output:
        {"a":[1,2],"b":[3,4]}'''

data = {"a":[1,2,2],"b":[3,3,4]}

for key, value in data.items():
    data[key] = list(set(value))

print(data)