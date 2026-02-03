'''28. Closure Access Counter
        Input: call f() 3 times
        Output: 1, 2, 3'''

user_input = int(input("enter value for call function:"))

def print_value(value):
    print(value, end=', ')

for number in range(1, user_input + 1):
    print_value(number)
print()