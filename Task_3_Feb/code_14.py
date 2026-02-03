'''14. Class-level vs Instance-level Attributes
Input: Set `cls.count = 0` and modify inside __init__
Output: Different values for class and instance'''

class MyClass:

    count = 0

    def __init__(self, value):
        
        self.count = value

obj1 = MyClass(10)
obj2 = MyClass(20)

print(f"Class count: {MyClass.count}")
print(f"obj1 instance count: {obj1.count}")
print(f"obj2 instance count: {obj2.count}")

MyClass.count = 50
print(f"\nClass count after modification: {MyClass.count}")
print(f"obj1 instance count is unchanged: {obj1.count}")
print(f"obj2 instance count is unchanged: {obj2.count}")
