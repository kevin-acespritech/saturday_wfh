'''9. Symmetric Difference of SetsInput: A = {1, 2, 3}, B = {3, 4, 5}
      Output: {1, 2, 4, 5}'''

A = {1, 2, 3}
B = {3, 4, 5}

result = (A | B).difference(A & B)
print(result)


