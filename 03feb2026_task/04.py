'''4. Flatten a Nested List
      Input: [1, [2, 3], [4, [5, 6]], 7]
      Output: [1, 2, 3, 4, 5, 6, 7]'''

input = [1, [2, 3], [4, [5, 6]], 7]
result = []

def flatten_list(list):
    for element in list:
        if isinstance(element, int):
            result.append(element)
        else:
            flatten_list(element)
        
flatten_list(input)
print(result)
