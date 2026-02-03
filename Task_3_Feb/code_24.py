'''24. CSV to Dictionary
Input CSV: name,age\nAlice,30\nBob,25
Output: [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]'''
import csv

csv_data = """name,age
Alice,30
Bob,25
"""

result = list(csv.DictReader(csv_data.splitlines()))

print(result)