'''1. Merge a list of dictionaries by summing values of common keys.
        Input:
        [{"a":10,"b":20},{"a":5,"c":15},{"b":10,"c":5}]
        Output:
        {"a":15,"b":30,"c":20}'''


data = [{"a":10,"b":20},{"a":5,"c":15},{"b":10,"c":5}]
result = {}

for dict in data:
    for key, value in dict.items():
        if key in result:
            result[key] = result[key] + value
        else:
            result[key] = value

print(result)