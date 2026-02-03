'''15. Method Overriding Example
        Input: class A, class B(A)
        Output: Prints from overridden method in B'''

class Animal:
    def display(self):
        print("animal eats!")

class Domestic_animal(Animal): 
    def display(self): 
        print("eats veg food!")

cow = Domestic_animal()

cow.display()