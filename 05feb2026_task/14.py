'''14. Count total elements across all lists.
        Input:
        {"a":[1,2],"b":[3]}
        Output:
        3'''

data = {"a":[1,2],"b":[3]}
total_count = 0

for value in data.values():
    total_count += len(value)

print(total_count)