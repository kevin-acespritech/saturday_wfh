'''17. Custom Exception
Input: raise NegativeNumberError if input < 0
Output: "NegativeNumberError: Negative value not allowed"'''

class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise NegativeNumberError("Negative value not allowed")
    print("Valid number:", num)

except NegativeNumberError as e:
    print(e)
