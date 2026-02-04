'''24. Count occurrences using dict.
Input:
['a','b','a','c']
Output:
{'a':2,'b':1,'c':1}
'''

data = ['a','b','a','c']
answer = {}
for character in data:
    if character in answer:
        answer[character] += 1
    else:
        answer[character]= 1


print(answer)