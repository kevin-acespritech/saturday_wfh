'''Write a Python program that takes the given fruit inventory data and writes it to a CSV file (fruits.csv). The program should:

Create a CSV file with headers: Fruit, Category, Quantity, Price (per kg)

Each dictionary in the data should be written as a separate row in the CSV file.

data = [
    {'fruit': 'Apple', 'category': 'Citrus', 'quantity': 100, 'price_per_kg': 150},
    {'fruit': 'Banana', 'category': 'Tropical', 'quantity': 200, 'price_per_kg': 50},
    {'fruit': 'Mango', 'category': 'Tropical', 'quantity': 150, 'price_per_kg': 120},
    {'fruit': 'Orange', 'category': 'Citrus', 'quantity': 120, 'price_per_kg': 90},
    {'fruit': 'Grapes', 'category': 'Berry', 'quantity': 180, 'price_per_kg': 80},
    {'fruit': 'Strawberry', 'category': 'Berry', 'quantity': 90, 'price_per_kg': 200},
]


Fruit,Category,Quantity,Price (per kg)
Apple,Citrus,100,150
Banana,Tropical,200,50
Mango,Tropical,150,120
Orange,Citrus,120,90
Grapes,Berry,180,80
Strawberry,Berry,90,200'''

import csv

data = [
    {'fruit': 'Apple', 'category': 'Citrus', 'quantity': 100, 'price_per_kg': 150},
    {'fruit': 'Banana', 'category': 'Tropical', 'quantity': 200, 'price_per_kg': 50},
    {'fruit': 'Mango', 'category': 'Tropical', 'quantity': 150, 'price_per_kg': 120},
    {'fruit': 'Orange', 'category': 'Citrus', 'quantity': 120, 'price_per_kg': 90},
    {'fruit': 'Grapes', 'category': 'Berry', 'quantity': 180, 'price_per_kg': 80},
    {'fruit': 'Strawberry', 'category': 'Berry', 'quantity': 90, 'price_per_kg': 200},
]

with open('fruits.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Fruit', 'Category', 'Quantity', 'Price(per kg)'])

    for item in data:
        writer.writerow([
            item['fruit'],
            item['category'],
            item['quantity'],
            item['price_per_kg']
        ])

print("fruits.csv file created successfully!")