'''1. Recursive Digit Sum
      Input: 9875
      Output: 2 # (9+8+7+5 = 29 -> 2+9 = 11 -> 1+1 = 2)'''


user_input = input("enter number:")
string = user_input

while True:
    if int(string) > 0 and int(string) <= 9:
        print(string)
        break
    else:
        sum = 0
        for number in string:
            sum += int(number)

        string = str(sum)

