'''21. Diamond Pattern
        Input: 3
        Output:
         *
        ***
       *****
        ***
         * '''

number = 3

for row in range(1, number + 1):
    print("  " * (number - row) + "* " * (2 * row - 1))

for row in range(number - 1, 0, -1):
    print("  " * (number - row) + "* " * (2 * row - 1))
