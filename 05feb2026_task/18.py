'''18. Replace each element with row sum minus itself.
        Input:
        [[1,2],[3,4]]
        Output:
        [[2,1],[4,3]]
        '''

data = [[1,2],[3,4]]
length = len(data)
    
for row in range(length):
    total = sum(data[row])
    for column in range(length):
        data[row][column] = total - data[row][column]
    
print(data)