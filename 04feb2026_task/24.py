'''24. Count occurrences using dict.
        Input:
        ['a','b','a','c']
        Output:
        {'a':2,'b':1,'c':1}
        '''

data = ['a','b','a','c']
result = {}

# for value in data:
#     count = data.count(value)
#     result[value] = count
# print(result)


for word in data:
    counter = 0
    for temp_word in data:
        if word == temp_word:
            counter += 1
    
    result[word] = counter

print(result)

