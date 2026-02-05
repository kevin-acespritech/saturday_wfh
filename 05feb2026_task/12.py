'''12. Flatten dict of list to sorted unique list.
        Input:
        {"x":[3,1],"y":[2,3]}
        Output:
        [1,2,3]'''

data = {"x":[3,1],"y":[2,3]}
temp_list = []

for value in data.values():
    temp_list.extend(value)

unique_list = list(set(temp_list))
print(unique_list)