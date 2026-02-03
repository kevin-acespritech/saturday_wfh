'''4. Flatten a Nested List
Input: [1, [2, 3], [4, [5, 6]], 7]
Output: [1, 2, 3, 4, 5, 6, 7]'''

nested_list= [[1,[2,3],[4 , [5,6]] , 7]]
answer_list = [] 
def flatten_list(given_list):
    for element in given_list:
        if isinstance(element, list):
            flatten_list(element)
        else:
            answer_list.append(element)

flatten_list(nested_list)
print(answer_list)