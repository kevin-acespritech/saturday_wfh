'''21. Find sublist with max sum.
        Input:
        [[1,2],[5],[3,4]]
        Output:
        [3,4]'''

data = [[1,2],[5],[3,4]]
max_sum = 0
result = None

for list in data:
    if sum(list) > max_sum:
        max_sum = sum(list)
        result = list

print(result)