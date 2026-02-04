'''25. Merge two dictionaries.
Input:
{'a':1} and {'b':2}
Output:
{'a':1,'b':2}
'''
dict_one = {'a' : 1}
dict_two = {'b' : 2}

dict_one.update(dict_two)
print(dict_one)