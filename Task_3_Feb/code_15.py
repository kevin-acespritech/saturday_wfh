'''15. Method Overriding Example
Input: class A, class B(A)
Output: Prints from overridden method in B'''


class Animal:
    def speak(self):
        return "Some generic animal sound"
class Dog(Animal):    
    def speak(self):
        return "Woof! Woof!"
    
animal_sound = Animal()
dog_sound = Dog()

print(animal_sound.speak() ,  dog_sound.speak())