'''10. Group Anagrams
       Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
       Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]'''

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = []
temp = []


for value in input:
    target = value
    for word in input:
        for character in word:
            if character not in target:
                break
        else:
            temp.append(word)
    if temp not in result:
        result.append(temp)
    temp = []

print(result)
