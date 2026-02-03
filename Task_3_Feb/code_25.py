'''25. Custom Reduce (Multiply)
Input: [1, 2, 3, 4]
Output: 24'''
from functools import reduce

list_one = [1,2,3,4,5]
answer  = (reduce(lambda x , y : x* y, list_one ))
print(answer)