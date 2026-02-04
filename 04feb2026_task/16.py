'''16. Store product details.
        Input:
        {101:{'name':'Pen','price':10}}
        Output:
        Product 101 Pen 10'''

data = {101: {'name': 'Pen', 'price': 10}}

for key, value in data.items():
    print(f"Product {key} {value['name']} {value['price']}")

