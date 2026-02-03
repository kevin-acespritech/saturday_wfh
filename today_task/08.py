'''8. Find Missing Number Using Sets
      Input: A = [1, 2, 3, 4], B = [1, 2, 4]
      Output: Missing: 3'''

A = [1, 2, 3, 4]
B = [1, 2, 4]

set_1 = set(A)
set_2 = set(B)

result = set_1.difference(set_2)
print(result)
