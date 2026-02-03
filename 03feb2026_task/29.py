'''29. Dict to Key=Value Strings
        Input: {'a': 1, 'b': 2}
        Output: ['a=1', 'b=2']'''

data = {'a': 1, 'b': 2}
result = []

for key, value in data.items():
    result.append(f"{key}={value}")

print(result)