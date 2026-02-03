'''11. Merge Nested Dictionaries
Input:
a = {'x': {'a': 1}}, b = {'x': {'b': 2}}
Output: {'x': {'a': 1, 'b': 2}}'''

a = {'x': {'a': 1}}
b = {'x': {'b': 2}}

anwser = {}

for key in a.keys() | b.keys():
    if key in a and b:
        anwser[key]={**a[key] , **b[key]}

print(anwser)