# Inheritance - It allows class to inherit attributes and methods from another class.
#               Helps with the code reusability
#               class Child(Parent)

class Parent:
    def greet(self):
        print("Hello from Parent!")

class Child(Parent):
    def greet(self):  # Overriding the parent method
        print("Hello from Child!")

    def child_only_method(self):
        print("This method exists only in Child.")

# Usage
c = Child()
c.greet()              # Output: Hello from Child!
c.child_only_method()  # Output: This method exists only in Child.



class Animal:
  def __init__(self, name):
    self.name =name
  def eat(self):
    return f"{self.name} is eating."
  
  def sleeping(self):
    return f"{self.name} is sleeping"
  
class Dog(Animal):
    pass
  
class Duck(Animal):
    pass
  
class Horse(Animal):
    pass



dog_1 = Dog("Scoopy")
duck_1 = Duck("Mariane")
horse_1 = Horse("Gerald")


print(dog_1.eat())
print(dog_1.sleeping())

print(duck_1.eat())
print(horse_1.name)
print(horse_1.sleeping())  