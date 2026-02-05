'''13. Find key with longest list.
        Input:
        {"a":[1],"b":[1,2,3]}
        Output:
        "b"
        '''

data = {"a":[1],"b":[1,2,3]}
longest_list  = 0
answer = None

for key,values in data.items():
    if len(values) > longest_list:
        longest_list = len(values)
        answer = key
print(f"{answer} has a longest list!")