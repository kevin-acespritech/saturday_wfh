'''24. Find outer key with maximum inner sum.
        Input:
        {"p1":{"a":10},"p2":{"a":20}}
        Output:
        "p2"
        '''

data = {"p1":{"a":10},"p2":{"a":20}}
max_key = None
max_value = 0

def find_max(data, parent_key=''):
    global max_key
    global max_value
    for key, value in data.items():
        if isinstance(value, dict):
            find_max(value, key)
        else:
            sum(data.values())
            if value > max_value:
                max_value = value
                max_key = parent_key
find_max(data)
print(max_key)
print(max_value)