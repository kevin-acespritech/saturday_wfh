'''13. Duplicate Characters in String
Input: "programming"
Output: ['r', 'g', 'm']'''

sample_list = "programming"
answer = []
for character in (sample_list):
    count  = sample_list.count(character)
    if count > 1 and character not in answer:
        answer.append(character)
    
print(answer)