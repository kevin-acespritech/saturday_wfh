'''22. Number Pyramid
        Input: 3
        Output:
          1
         2 2
        3 3 3'''

n = 5

for i in range(1, n + 1):
    print("  " * (n - i), end=" ")
    
    for j in range(1, i + 1):
        print(i, end=" ")
        if j < i:
            print(" ", end=" ")
    print()