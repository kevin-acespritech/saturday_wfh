'''11. Merge Nested Dictionaries
        Input:
        a = {'x': {'a': 1}}, b = {'x': {'b': 2}}

        Output: {'x': {'a': 1, 'b': 2}}'''

a = {'x': {'a': 1}}
b = {'x': {'b': 2}}
result = {}

def merge_dict(dict_1, dict_2):

    for key in dict_1.keys() | dict_2.keys():
        if key in dict_1 and dict_2:
            result[key] = {**dict_1[key], **dict_2[key]}
    print(result)

merge_dict(a, b)