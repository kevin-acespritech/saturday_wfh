'''18. Update product stock.
        Input:
        {'stock':5} → update to 8
        Output:
        Stock updated'''

data = {'stock':5}

if 'stock' in data:
    data['stock'] = 8
    print("Stock updated")
else:
    print("key does not exist!")