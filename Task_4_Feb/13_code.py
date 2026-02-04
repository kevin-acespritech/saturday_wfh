'''13. Convert list of lists to flat list.
Input:
[[1,2],[3,4]]
Output:
[1,2,3,4]'''


given_list = [[1,2],[3,4]]
def nested_to_flatten(given_list):
    flatten_list = []
    for element in given_list:
        if isinstance(element , list):
            flatten_list.extend(nested_to_flatten(element))
        else:
            flatten_list.append(element)

    return flatten_list

answer = nested_to_flatten(given_list)
print(answer)