'''22. Number Pyramid
Input: 3
Output:
1
22
33'''

number = int(input("Enter number: "))

for row in range(1, number + 1):    
    print(" " * (2 * (number - row)), end="")

    for column in range(row):
        print(row, end="   ")

    print()
