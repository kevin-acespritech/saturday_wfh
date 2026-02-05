'''20. Flatten list of lists.
        Input:
        [[1,2],[3,4]]
        Output:
        [1,2,3,4]'''

data = [[1,2],[3,4]]
result = []
for value in data:
    result += value
print(result)