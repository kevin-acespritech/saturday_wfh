'''23. Sort list of dictionaries by key.
Input:
[{'age':30},{'age':20}]
Output:
[{'age':20},{'age':30}]'''

data = [{'age':30},{'age':20}]
answer = sorted(data,key = lambda x: x['age']) 
print(answer)