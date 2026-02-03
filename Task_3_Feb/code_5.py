'''5. List Rotation (Left by K)
Input: lst = [1, 2, 3, 4, 5], k = 2
Output: [3, 4, 5, 1, 2]'''

input_list = [1,2,3,4,5]
target = 2
index_number = input_list.index(target+1)
for number in range(index_number):
    first_number = input_list.pop(0)
    input_list.append(first_number)
print(input_list)