'''6. Find Pairs With Sum
Input: lst = [1, 5, 7, -1, 5], target = 6
Output: [(1, 5), (7, -1)]'''


input_list = [1,5,7,-1,5]
target = 6
result_list = []

for number1 in range (len(input_list)):
    for number2 in range (input_list[number1] + 1,  len(input_list)):
        if (input_list[number1] + input_list[number2]) == target:
            
            result_list.append((input_list[number1] ,input_list[number2]))
print(result_list)
