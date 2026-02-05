'''4. Find the key whose total value across dictionaries is maximum.
        Input:
        [{"x":10,"y":20},{"x":5,"y":30}]
        Output:
        "y"'''

data = [{"x":10,"y":20},{"x":5,"y":30}]

result = {}
id = None
max_total = 0

for dict in data:
    for key, value in dict.items():
        if key in result:
            result[key] = result[key] + value
            if result[key] > max_total:
                max_total = result[key]
                id = key
        else:
            result[key] = value

print(f"{id} highest total value")