'''13. Duplicate Characters in String
        Input: "programming"
        Output: ['r', 'g', 'm']'''

input = 'programming'
result = []

for character in input:
    count = input.count(character)
    if count > 1 and character not in result:
        result.append(character)
        
print(result)