'''26. Lambda With Condition
Input: [1, 2, 3, 4]
Output: ['Odd', 'Even', 'Odd', 'Even']'''

given_list = [1,2,3,4,5]
answer = list(map(lambda x : "even" if x%2 ==0 else  "odd" , given_list))
print(answer)