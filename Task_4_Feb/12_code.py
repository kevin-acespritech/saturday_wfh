'''12. Find maximum value from list of lists.
Input:
[[1,2,3],[4,5,6]]
Output:
Maximum = 6
'''

given_list = [[1,2,3],[4,5,6]]

def find_max_nested_list(lst):
    max_value = 0
    for element in lst:
        if isinstance(element , list):
            nested_max = find_max_nested_list(element)
            if nested_max > max_value:
                max_value = nested_max
        else:
            
            if element > max_value:
                max_value = element


    return max_value
a = find_max_nested_list(given_list)
print(a)