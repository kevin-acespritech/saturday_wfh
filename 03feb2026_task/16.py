'''16. Operator Overloading
        Input:
        v1 = Vector(1, 2); v2 = Vector(3, 4); v1 + v2
        Output: Vector(4, 6)'''

class Vector:
    def __init__(self, value_1, value_2):
        self.value_1 = value_1
        self.value_2 = value_2

    def __add__(self, other):
        return Vector(self.value_1 + other.value_1, self.value_2 + other.value_2)
    
    def __str__(self):
        return f"Vector({self.value_1}, {self.value_2})"

    
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v = v1 + v2
print(v)
