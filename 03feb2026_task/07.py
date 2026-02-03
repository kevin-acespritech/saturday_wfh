'''7. Modify a Tuple (Tricky Immutability)
      Input: tup = (1, [2, 3], 4); tup[1].append(5)
      Output: (1, [2, 3, 5], 4)'''

input_tup = (1, [2, 3], 4)
input_tup[1].append(5)
print(input_tup)