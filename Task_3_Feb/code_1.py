'''1. Recursive Digit Sum
Input: 9875
Output: 2 # (9+8+7+5 = 29 -> 2+9 = 11 -> 1+1 = 2)'''

def sum_recursive(number):
    sum = 0
    while number > 0 or sum > 9:
        if number == 0:
            number = sum
            sum = 0
        sum = sum + number % 10
        number = number // 10
    return sum

answer = sum_recursive(9875)
print(answer)