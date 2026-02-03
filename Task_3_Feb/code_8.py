'''8. Find Missing Number Using Sets
Input: A = [1, 2, 3, 4], B = [1, 2, 4]
Output: Missing: 3'''

list_one = [1,2,3,4]
list_two = [1,2,4]

answer = set(list_one).difference(set(list_two))
print(answer)