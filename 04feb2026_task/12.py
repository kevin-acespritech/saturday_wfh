'''12. Find maximum value from list of lists.
        Input:
        [[1,2,3],[4,5,6]]
        Output:
        Maximum = 6
'''

sample_list = [[1,2,3],[4,5,6]]
max_value = 0

def find_maximum(samp_list):
    global max_value

    for value in samp_list:
        if isinstance(value, list):
            find_maximum(value)
        else:
            if value > max_value:
                max_value = value

    return max_value

print(f"maximum = {find_maximum(sample_list)}")