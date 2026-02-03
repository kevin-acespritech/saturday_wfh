''''29. Dict to Key=Value Strings
Input: {'a': 1, 'b': 2}
Output: ['a=1', 'b=2']'''

ans_list= []

sample_data = {'a': 1, 'b': 2}
for key , value  in sample_data.items():
    answer = f"{key}={value}"
    ans_list.append(answer)
print(ans_list)
