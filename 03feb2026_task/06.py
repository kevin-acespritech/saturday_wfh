'''6. Find Pairs With Sum
      Input: lst = [1, 5, 7, -1, 5], target = 6
      Output: [(1, 5), (7, -1)]'''

sample_list = [1, 5, 7, -1, 5]
target = 6
result = []

for number_1 in range(len(sample_list)):
    for number_2 in range(number_1 + 1, len(sample_list)):
        if (sample_list[number_1] + sample_list[number_2]) == target and (sample_list[number_1], sample_list[number_2]) not in result:
            result.append((sample_list[number_1], sample_list[number_2]))
print(result)