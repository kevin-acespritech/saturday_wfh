'''23. Read File Word Count
        Input: "hello world hello"
        Output: {'hello': 2, 'world': 1}'''

user_input = "hello world hello"
answer= {}

temp_list = input.split(" ")

for word in temp_list:
    count = temp_list.count(word)
    answer[word] = count
print(answer)