'''16. Rotate matrix 90 degrees clockwise.
        Input:
        [[1,2],[3,4]]
        Output:
        [[3,1],[4,2]]
        '''

data = [[1,2],[3,4]]


length = len(data)
    
for row in range(length):
    for column in range(row, length):
        data[row][column], data[column][row] = data[column][row], data[row][column]

for index in range(length):
    data[index].reverse()

print(data)