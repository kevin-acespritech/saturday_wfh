# 1. Store student details and display them.
# Input:
# students = [
#  {'name':'Aarav','age':20,'marks':85},
#  {'name':'Diya','age':22,'marks':90}
# ]
# Output:
# Aarav 20 85
# Diya 22 90

students = [
    {'name': 'Aarav', 'age': 20, 'marks': 85},
    {'name': 'Diya', 'age': 22, 'marks': 90}
]

for student in students:
    print(student['name'], student['age'], student['marks'])

# 2. Find student with highest marks.
# Input:
# [{'name':'A','marks':70},{'name':'B','marks':90}]
# Output:
# B has highest marks  

names = ['A', 'B']
marks = [70, 90]

highest_marks = marks[0]
highest_name = names[0]

for i in range(1, len(marks)):
    if marks[i] > highest_marks:
        highest_marks = marks[i]
        highest_name = names[i]

print(highest_name, "has highest marks")

# 3. Count number of students.
# Input:
# [{'id':1},{'id':2},{'id':3}]
# Output:
# Total students = 3 

students = [{'id':1}, {'id':2}, {'id':3}]

total = len(students)

print("Total students =", total)

# 4. Update marks of a student.
# Input:
# {'name':'Rahul','marks':60} → update to 75
# Output:
# {'name':'Rahul','marks':75}

student = {'name':'Rahul','marks':60}

student['marks'] = 75

print(student)

# 5. Remove a student by name.
# Input:
# ['Amit','Neha','Ravi']
# Remove: Neha
# Output:
# ['Amit','Ravi']

students = ['Amit', 'Neha', 'Ravi']

students.remove('Neha')

print(students)

# DICTIONARY OF LISTS

# 6. Store employee data and display row-wise.
# Input:
# {'name':['Rohit','Sneha'],'salary':[50000,60000]}
# Output:
# Rohit 50000
# Sneha 60000 

employee = {'name': ['Rohit', 'Sneha'], 'salary': [50000, 60000]}

for i in range(len(employee['name'])):
    print(employee['name'][i], employee['salary'][i])

# 7. Find average salary.
# Input:
# {'salary':[30000,40000,50000]}
# Output:
# Average salary = 40000

n = int(input("Enter number of employees: "))
salaries = []

for i in range(n):
    salary = int(input("Enter salary of employee: "))
    salaries.append(salary)

total = 0
for s in salaries:
    total += s

average = total // n  

print("Average salary =", average)

# 8. Add new employee details.
# Input:
# {'name':['A'],'salary':[20000]}
# Add: B, 30000
# Output:
# {'name':['A','B'],'salary':[20000,30000]}

employee = {'name': ['A'], 'salary': [20000]}

new_name = 'B'
new_salary = 30000

employee['name'].append(new_name)
employee['salary'].append(new_salary)

print(employee)

# 9. Count total employees.
# Input:
# {'name':['A','B','C']}
# Output:
# Total employees = 3

employee = {'name': ['A', 'B', 'C']}

total = len(employee['name'])

print(total)

# 10. Find highest salary.
# Input:
# {'salary':[25000,45000,30000]}
# Output:
# Highest salary = 45000

n = int(input("Enter number of employees: "))
highest = 0

for i in range(n):
    salary = int(input("Enter salary of employee: "))
    if salary > highest:
        highest = salary

print("Highest salary =", highest)

# LIST OF LISTS

# 11. Store marks and calculate total.
# Input:
# [['Anu',80,90],['Raj',70,75]]
# Output:
# Anu total = 170
# Raj total = 145

marks = [['Anu', 80, 90], ['Raj', 70, 75]]

for m in marks:
    total = m[1] + m[2] 
    print(m[0], "total =", total)

# 12. Find maximum value from list of lists.
# Input:
# [[1,2,3],[4,5,6]]
# Output:
# Maximum = 6

list2 = [[1,2,3],[4,5,6]]
max = 0

for i in list2:
    for num in i:
     if num > max:
        max = num
print(max)

# 13. Convert list of lists to flat list.
# Input:
# [[1,2],[3,4]]
# Output:
# [1,2,3,4] 

lists = [[1, 2], [3, 4]]
new_list = []

for i in lists:
    for number in i:
        new_list.append(number)

print(new_list)

#  14. Count number of rows.
# Input:
# [[1,2],[3,4],[5,6]]
# Output:
# Rows = 3
 
lists = [[1,2],[3,4],[5,6]]
rows = 0

for row in lists:
    rows = rows + 1

print("Rows =", rows)


# 15. Find student with highest total.
# Input:
# [['A',50,50],['B',60,70]]
# Output:
# B

students1 = [['A',50,50],['B',60,70]] 
highest = 0
for students in students1:
    name = students[0]
    total = students[1] + students[2]

    if total > highest:
        highest = total
        
print(name)

# DICTIONARY OF DICTIONARIES

# 16. Store product details.
# Input:
# {101:{'name':'Pen','price':10}}
# Output:
# Product 101 Pen 10

products = {101: {'name': 'Pen', 'price': 10}}

for id in products:
    print("Product", id, products[id]['name'], products[id]['price'])

# 17. Find product with highest price.
# Input:
# {1:{'price':10},2:{'price':20}}
# Output:
# Product ID 2

products = {1: {'price': 10}, 2: {'price': 20}}

max_price = 0
max_id = 0

for id in products:
    if products[id]['price'] > max_price:
        max_price = products[id]['price']
        max_id = id

print("Product ID", max_id)

# 18. Update product stock.
# Input:
# {'stock':5} → update to 8
# Output:
# Stock updated
product = {'stock': 5}

product.update({'stock': 8})  

print("Stock updated")

# 19. Delete a product.
# Input:
# {1:{},2:{}}
# Delete key:1
# Output:
# {2:{}}
products = {1: {}, 2: {}}

del products[1]  

print(products)

# 20. Count total products.
# Input:
# {1:{},2:{},3:{}}
# Output:
# Total products = 3

products = {1: {}, 2: {}, 3: {}}

count = 0
for p in products:
    count = count + 1

print(count)

# MIXED PROGRAMS
# 21. Find average marks using list of dict.
# Input:
# {'marks':[80,90,100]}
# Output:
# Average = 90

data = {'marks': [80, 90, 100]}

total = 0
count = 0

for m in data['marks']:
    total = total + m
    count = count + 1

average = total // count

print(average)

# 22. Convert dictionary of lists to list of dicts.
# Input:
# {'name':['A','B'],'age':[20,22]}
# Output:
# [{'name':'A','age':20},{'name':'B','age':22}]

data = {'name': ['A', 'B'], 'age': [20, 22]}

result = []

for i in range(2):
    result.append({'name': data['name'][i], 'age': data['age'][i]})

print(result)

# 23. Sort list of dictionaries by key.
# Input:
# [{'age':30},{'age':20}]
# Output:
# [{'age':20},{'age':30}]

data = [{'age': 30}, {'age': 20}]

data = sorted(data, key=lambda x: x['age'])

print(data)

# 24. Count occurrences using dict.
# Input:
# ['a','b','a','c']
# Output:
# {'a':2,'b':1,'c':1}

items = ['a', 'b', 'a', 'c']
count = {}

for i in items:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1

print(count)

# 25. Merge two dictionaries.
# Input:
# {'a':1} and {'b':2}
# Output:
# {'a':1,'b':2}

dict1 = {'a': 1}
dict2 = {'b': 2}

merged = dict1 | dict2
print(merged)
dict1.update(dict2)
print(dict1)

