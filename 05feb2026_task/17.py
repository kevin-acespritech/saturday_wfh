'''17. Remove sublists whose sum is even.
        Input:
        [[1,2],[3,3],[4,5]]
        Output:
        [[4,5]]'''

data = [[1,2],[3,3],[4,5]]
result = []

for list in data:
    if sum(list) % 2 != 0:
        result.append(list)
print(result)