'''13. Convert list of lists to flat list.
        Input:
        [[1,2],[3,4]]
        Output:
        [1,2,3,4]'''

result_list = []

def flatten_list(samp_list):
    for value in samp_list:
        if isinstance(value, list):
            flatten_list(value)
        else:
            result_list.append(value)

    return result_list

answer = flatten_list([[1,2],[3,4]])
print(answer)