'''7. Modify a Tuple (Tricky Immutability)
Input: tup = (1, [2, 3], 4); tup[1].append(5)
Output: (1, [2, 3, 5], 4)'''
tuple_given = (1, [2, 3], 4)
tuple_given[1].append(5)
print(tuple_given)