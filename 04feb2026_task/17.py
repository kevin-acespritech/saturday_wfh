'''17. Find product with highest price.
        Input:
        {1:{'price':10},2:{'price':20}}
        Output:
        Product ID 2
        '''

data = {1:{'price':10},2:{'price':20}}
max_value = 0
id = None
for product in data:
    for value in data[product].values():
        if value > max_value:
            max_value = value
            id = product
        
print(f"product ID {id}")
