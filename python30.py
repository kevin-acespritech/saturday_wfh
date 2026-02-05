#1
list = [{"a":10,"b":20},{"a":5,"c":15},{"b":10,"c":5}]
result = {}

for i in list:
    for key in i:
        if key in result:
            result[key] += i[key]
        else:
            result[key] = i[key]
print(result)

#2
data = [{"a":1,"b":2},{"b":2,"a":1},{"a":2,"b":3}]
unique = []

for i in data:
    if i not in unique:
        unique.append(i)
print(unique)

#3
data = [{"a":0,"b":0},{"a":1,"b":0},{"a":0,"b":2}]
result = []

for i in data:
    if any(i.values()):
        result.append(i)
print(result)

#4
data = [{"x":10,"y":20},{"x":5,"y":30}]
total = {}

for i in data:
    for k in i:
        total[k] = total.get(k,0)+i[k]
max_key = max(total,key = total.get)
print(max_key)

#5
data  = [{"name":"A","score":90},{"name":"B","score":80}]

result = {"name":[],"score": []}

for i in data:
    result["name"].append(i["name"])
    result["score"].append(i["score"])
print(result)

#6
data = [{"a":1,"b":2},{"a":5},{"a":2,"b":1}]

for i in range(len(data)):
    for j in range(i+1 , len(data)):
        if sum(data[i].values()) > sum(data[j].values()):
            data[i],data[j] = data[j],data[i]
print(data)

#7
data = [{"a":1},{"b":2}]
keys = set()

for i in data:
    keys.update(i.keys())

result = []
for i in data:
    new_dict = {}
    for k in keys:
        new_dict[k] = i.get(k,0)
    result.append(new_dict)
print(result)

#8
data = [{"a":1,"b":1},{"a":1,"b":2}]

max_dict = data[0]

for d in data:
    if len(set(d.values())) > len(set(max_dict.values())):
        max_dict = d

print( max_dict)

# #9
# data = {"a":[1,2,2],"b":[3,3,4]}

# for k in data:
#     data[k] = list(set(data[k]))

# print(data)

#10
data = {"a":[1,2],"b":[2,3]}
result = {}

for k in data:
    for val in data[k]:
        if val not in result:
            result[val] = []
        result[val].append(k)

print(result)

#11
data = {"a":[1,2],"b":[10],"c":[2,2]}
result = {}

for k in data:
    if sum(data[k]) >= 5:
        result[k] = data[k]

print(result)

#12
data = {"x":[3,1],"y":[2,3]}
result = []

for v in data.values():
    for i in v:
        if i not in result:
            result.append(i)

result.sort()
print(result)

#13
data = {"a":[1],"b":[1,2,3]}
longest = ""

for k in data:
    if longest == "" or len(data[k]) > len(data[longest]):
        longest = k

print(longest)

#14
data = {"a":[1,2],"b":[3]}
count = 0

for v in data.values():
    count += len(v)

print(count)

#15 
data = {"a":[2,4],"b":[1,3,5]}
result = {}

for k in data:
    result[k] = sum(data[k]) // len(data[k])

print(result)

#16
mat = [[1,2],[3,4]]
rotated = []

for i in range(len(mat)):
    row = []
    for j in range(len(mat)-1, -1, -1):
        row.append(mat[j][i])
    rotated.append(row)

print(rotated)

#17 
data = [[1,2],[3,3],[4,5]]
result = []

for lst in data:
    if sum(lst) % 2 != 0:
        result.append(lst)

print(result)

#18

mat = [[1,2],[3,4]]
result = []

for row in mat:
    total = sum(row)
    new_row = []
    for x in row:
        new_row.append(total - x)
    result.append(new_row)

print(result)

#19
mat = [[1,2,3],[4,5,6],[7,8,9]]
diag = []

for i in range(len(mat)):
    diag.append(mat[i][i])

print(diag)

#20

data = [[1,2],[3,4]]
flat = []

for lst in data:
    for x in lst:
        flat.append(x)

print(flat)

#21

data = [[1,2],[5],[3,4]]
max_list = data[0]

for lst in data:
    if sum(lst) > sum(max_list):
        max_list = lst

print(max_list)

#22

data = [[1,2],[2,1],[1,2]]
result = []

for lst in data:
    if lst not in result:
        result.append(lst)

print(result)

#23

data = {"a":{"x":1},"b":{"y":2}}
result = {}

for k in data:
    for ik in data[k]:
        result[k + "." + ik] = data[k][ik]

print(result)

#24

data = {"p1":{"a":10},"p2":{"a":20}}
max_key = ""

for k in data:
    if max_key == "" or sum(data[k].values()) > sum(data[max_key].values()):
        max_key = k

print(max_key)

#25

data = {"x":{"a":1},"y":{"a":2}}
result = {}

for k in data:
    for ik in data[k]:
        if ik not in result:
            result[ik] = {}
        result[ik][k] = data[k][ik]

print(result)

#26

data = {"a":{"x":0,"y":2},"b":{"x":1,"y":0}}
result = {}

for k in data:
    result[k] = {}
    for ik in data[k]:
        if data[k][ik] != 0:
            result[k][ik] = data[k][ik]

print(result)

#27 
d1 = {"a":{"x":1}}
d2 = {"a":{"x":4,"y":2}}
result = {}

for d in (d1, d2):
    for k in d:
        if k not in result:
            result[k] = {}
        for ik in d[k]:
            result[k][ik] = result[k].get(ik, 0) + d[k][ik]

print(result)

#28
data = {"a":{"x":1,"y":2},"b":{"z":3}}
count = 0

for v in data.values():
    count += len(v)

print(count)

# #29
# data = {"a":{"x":1,"y":2},"b":{"x":5}}
# common = set(data["a"].keys())

# for v in data.values():
#     common = common & set(v.keys())

# print(list(common))

#30 
data = {"a":{"x":1},"b":{"y":2}}
result = []

for k in data:
    for ik in data[k]:
        result.append((k, ik, data[k][ik]))

print(result)