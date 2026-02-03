'''5. List Rotation (Left by K)
      Input: lst = [1, 2, 3, 4, 5], k = 2
      Output: [3, 4, 5, 1, 2]'''

sample_list = [1, 2, 3, 4, 5]
target = 2
result = []

target_index = sample_list.index(target)

for index, value in enumerate(sample_list * 2):
    if index > target_index:
        if value != target:
            result.append(value)
        else:
            result.append(value)
            break
print(result)