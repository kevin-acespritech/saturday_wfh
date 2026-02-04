'''25. Merge two dictionaries.
    Input:
    {'a':1} and {'b':2}
    Output:
    {'a':1,'b':2}
    '''

dict_1 = {'a':1}
dict_2 = {'b':2}

answer = {**dict_1, **dict_2}
print(answer)