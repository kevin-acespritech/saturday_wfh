'''2. Custom Map Function
      Input: square = lambda x: x*x, lst = [1, 2, 3]
      Output: [1, 4, 9]'''

input = lambda x: x*x
lst = [1, 2, 3]

result = list(map(input, lst))
print(result)