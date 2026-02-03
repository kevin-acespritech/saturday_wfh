'''23. Read File Word Count
        Input: "hello world hello"
        Output: {'hello': 2, 'world': 1}'''

input = "hello world hello"
result = {}

temp_list = input.split(" ")

for word in temp_list:
    count = temp_list.count(word)
    result[word] = count
print(result)