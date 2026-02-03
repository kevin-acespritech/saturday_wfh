'''12. Longest Palindromic Substring
    Input: "babad"
    Output: "bab" or "aba"'''

input = "babad"

def longest_palindrome(string):

    result = []
    for i in range(len(string)):
        for j in range(i, len(string)): 
            b = string[i:j+1]         
            if len(b) > 1:
                if b == b[::-1]:
                    result.append(b)
            else:
                continue
    return result

print(longest_palindrome(input))