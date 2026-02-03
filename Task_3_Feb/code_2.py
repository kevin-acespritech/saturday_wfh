'''2. Custom Map Function
Input: square = lambda x: x*x, lst = [1, 2, 3]
Output: [1, 4, 9]'''

numeber_one = lambda n: n*n
list_number = [1,2,3,4,5]
answer = list(map(numeber_one,list_number))
print(answer)