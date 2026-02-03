# a = 9875

# while a > 9 :
#     s = 0 
#     for i in str(a):
#         s = s + int(i)
#     a = s

# print(a)

# square = lambda x: x*x
# lst = [1, 2, 3]

# result = []

# for i in lst:
#     result.append(square(i))

# print(result)

# x = 10

# def test():
#     print(x)
#     x = 5
# test()

# data = [1, [2, 3], [4, [5, 6]], 7]

# result = []

# for i in data:
#     if type(i) == list:
#         for j in i:
#             if type(j) == list:
#                 for k in j:
#                     result.append(k)
#             else:
#                 result.append(j)
#     else:
#         result.append(i)

# print(result)


# lst = [1, 2, 3, 4, 5]
# k = 2

# k = k%len(lst)

# result = lst[k:] + lst[:k]

# print(result)

# lst = [1, 5, 7, -1, 5]
# target = 6

# for i in range(len(lst)):
#     for j in range(i+1):
#         if lst[i]+lst[j] == target:
#             print("Pair:",(lst[i],lst[j]))

# tup = (1, [2, 3], 4)
# tup[1].append(5)
# print(tup)

# A = [1, 2, 3, 4]
# B = [1, 2, 4]

# missing =  sum(A)-sum(B)
# print(missing)

# A = {1, 2, 3}
# B = {3, 4, 5}

# result = A ^ B
# print(result)

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# result = []

# for w in words:
#     found = False

#     for group in result:
#         if sorted(group[0]) == sorted(w):
#             group.append(w)
#             found = True
#             break
#     if not found:
#         result.append([w])
# print(result)

# a = {'x': {'a': 1}}
# b = {'x': {'b': 2}}

# a["x"].update(b["x"])

# print(a)

# s = "programming"
# result = []

# for ch in s:
#     if s.count(ch) > 1 and ch not in result:
#         result.append(ch)

# print(result)

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# obj = B()
# obj.show()

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)

# v1 = Vector(1, 2)
# v2 = Vector(3, 4)

# v3 = v1 + v2

# print(v3.x, v3.y)

# try:
#     f = open("no_file.txt")
#     data = f.read()
#     print(data)

# except FileNotFoundError:
#     print("File does not exist!")

# import datetime

# today = datetime.date.today()      
# birthday = datetime.date(2025, 12, 25)

# days_left = (birthday - today).days

# print("Days left:", days_left)

# import datetime

# start = datetime.date(2025, 7, 1)
# end = datetime.date(2025, 7, 4)

# dates = []

# while start <= end:
#     dates.append(str(start))
#     start += datetime.timedelta(days=1)

# print(dates)

# n = 3

# for i in range(1, n+1):
#     spaces = n - i
#     stars = 2*i - 1
#     print(" " * spaces + "*" * stars)

# for i in range(n-1, 0, -1):
#     spaces = n - i
#     stars = 2*i - 1
#     print(" " * spaces + "*" * stars)

# n = 3

# for i in range(1, n+1):
#     print(" " * (n - i), end="")
    
#     for j in range(i):
#         print(i, end=" ")
    
#     print() 

# text = "hello world hello"

# words = text.split() 
# count = {}

# for word in words:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1

# print(count)

# lst = [1, 2, 3, 4]

# result = 1

# for num in lst:
#     result *= num

# print(result)

# lst = [1, 2, 3, 4]

# result = []

# for num in lst:
#     if num % 2 == 0:
#         result.append("Even")
#     else:
#         result.append("Odd")

# print(result)

# d = {'a': 1, 'b': 2}

# result = []

# for k, v in d.items():
#     result.append(k + "=" + str(v))

# print(result)

# a = 5
# b = 7

# a, b = b, a

# print(a, b)


