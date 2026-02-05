'''19. Find diagonal elements.
        Input:
        [[1,2,3],[4,5,6],[7,8,9]]
        Output:
        [1,5,9]'''

data = [[1,2,3],[4,5,6],[7,8,9]]
diagonal = []
length = len(data)



for row in range(length):
    for column in range(length):
        if row == column:
            diagonal.append(data[row][column])

print(diagonal)