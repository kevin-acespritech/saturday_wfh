'''16. Store product details.
Input:
{101:{'name':'Pen','price':10}}
Output:
Product 101 Pen 10'''

given_data = {101:{'name':'Pen','price':10}}

for key , value in given_data.items():
    print(f"Product {key} , {value['name']} { value['price']}") 