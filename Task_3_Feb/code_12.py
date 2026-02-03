'''12. Longest Palindromic Substring
Input: "babad"
Output: "bab" or "aba"'''

string_input =  "babad"

def longest_palindrome(string_input):
    answer = []
    
    for one in range(len(string_input)):
        for two in range(len(string_input)):
            temp = string_input[one : two +1]
            if len(temp) > 1:
                if temp == temp[::-1]:
                    answer.append(temp)
            else:
                continue

    return answer
print(longest_palindrome(string_input))
