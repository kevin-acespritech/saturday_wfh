#1
students = [
 {'name':'Aarav','age':20,'marks':85},
 {'name':'Diya','age':22,'marks':90}
]

for i in students:
    name = i["name"]
    age = i["age"]
    marks = i["marks"]
    print(name,age,marks)

#2
student = [
    {'name':'A','marks':70},
    {'name':'B','marks':90}
]

highest_marks = 0
topper_name  = ""

for i in student:
    if i["marks"] > highest_marks:
        highest_marks = i["marks"]
        topper_name = i["name"]
print(topper_name , "Has highest marks")

#3
students = [
    {'id':1},
    {'id':2},
    {'id':3},
]
count = 0

for i in students:
    count = count+1
print(count)

#4
student = {'name':'Rahul','marks':60}

student["marks"] = 75
print(student)

#5
student = ['Amit','Neha','Ravi']

remove_name = "Neha"
student.remove(remove_name)

print(student)

#6
employee  = {
    'name':['Rohit','Sneha'],
    'salary':[50000,60000]
}

for i in range(len(employee["name"])):
    name = employee["name"][i]
    salary = employee["salary"][i]
    print(name,salary)

#7
employee = {
    'salary':[30000,40000,50000]
}
total_salary = 0

for i in range(len(employee["salary"])):
    total_salary = total_salary+employee['salary'][i]
    avg_salary = total_salary/len(employee["salary"])
print(avg_salary)

#8
employee = {
    'name':['A'],
    'salary':[20000]
}

new_name = "B"
new_salary = 30000

employee["name"].append(new_name)
employee["salary"].append(new_salary)

print(employee)

#9
employee = {'name':['A','B','C']}

count = 0 
for i in range(len(employee['name'])):
    count = len(employee["name"])
print(count)

#10

employee = {'salary':[25000,45000,30000]}

max_salary = 0
for i in range(len(employee["salary"])):
    max_salary = max(employee["salary"])
print(max_salary)

#11
student = [
    ['Anu',80,90],
    ['Raj',70,75]
]

for i in student:
    name = i[0]
    marks1 = i[1]
    marks2 = i[2]

    total = marks1+marks2
    print(name,"Total marks = " ,total)

#12
list = [
    [1,2,3],
    [4,5,6]
]

max_value = max(list[0]+list[1])
print(max_value)

#13
list = [[1,2],[3,4]]

marg = list[0]+list[1]
print(marg)

#14
list = [
    [1,2],
    [3,4],
    [5,6]
]

row = len(list)
print(row)

#15
list = [['A',50,50],['B',60,70]]
highest_marks = 0
topper = ""
for i in list:
    name = i[0]
    marks1 = i[1]
    marks2 = i[2]

    total = marks1 + marks2

    if total > highest_marks:
        highest_marks = total
        topper = name
print(topper)

#16
products = {
    101: {'name': 'Pen', 'price': 10}
}

for i in products:
    name = products[i]["name"]
    price = products[i]["price"]

    print("Product",i,name,price)

#17
products = {1:{'price':10},2:{'price':20}}
highest_price = 0
product_id = 0

for pid in products:
    price = products[pid]['price']
    
    if price > highest_price:
        highest_price = price
        product_id = pid

print("Product ID", product_id)

#18

product = {'stock': 5}

product['stock'] = 8

print("Stock updated")

#19

products = {
    1: {},
    2: {}
}

delete_key = 1
del products[delete_key]

print(products)

#20 

products = {1:{},2:{},3:{}}

total_products = len(products)
print("Total products =", total_products)

#21

student = {'marks':[80,90,100]}

total = 0
for m in student['marks']:
    total = total + m

average = total / len(student['marks'])

print("Average =", average)

#22

data = {
    'name': ['A', 'B'],
    'age': [20, 22]
}

result = []

for i in range(len(data['name'])):
    d = {}
    d['name'] = data['name'][i]
    d['age'] = data['age'][i]
    result.append(d)

print(result)

#23

data = [
    {'age': 30},
    {'age': 20}
]

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i]['age'] > data[j]['age']:
            data[i], data[j] = data[j], data[i]

print(data)

#24
items = ['a', 'b', 'a', 'c']

count = {}

for item in items:
    if item in count:
        count[item] = count[item] + 1
    else:
        count[item] = 1

print(count)

#25
d1 = {'a': 1}
d2 = {'b': 2}
d1.update(d2)
print(d1)
