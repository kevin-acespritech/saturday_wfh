'''10. Group Anagrams
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]'''

ip_list= ["eat", "tea", "tan", "ate", "nat", "bat"]
def group_anagrams (ip_list):
    answer =  {}
    ip_list= ["eat", "tea", "tan", "ate", "nat", "bat"]

    for word in (ip_list):
        sorted_word = ''.join(sorted(word))

        if sorted_word in answer:
            answer[sorted_word].append(word)
        else:
            answer[sorted_word] = [word]

    return list(answer.values())


g= group_anagrams(ip_list)
print(g)