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


# this is superclass 
class Animal:
    def __init__(self, name): # parent cclass constructor
        self.name = name
        print(f"Animal created: {self.name}")
# The following code demonstrates the use of a superclass and subclass
# with the `super()` function to call the parent class constructor.
# while this is subclass 
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
        print(f"Dog breed: {self.breed}")

# Usage
d = Dog("Buddy", "Labrador")



# multiple inheritance = inherits more that 1 parent class  C(A, B)
# Multi-leve inheritance 
class Animal:
    def __init__(self, name):
        self.name =name
        
    def eat(self):
        return f"{self.name} is eating."
  
    def sleeping(self):
        return f"{self.name} is sleeping"

class Preditor(Animal):
    def hunt(self):
        return "The preditor is hunting"
    
class Prey(Animal):
    def flee(self):
        return "The prey is fleeing"
    
    
class Rabbit(Prey):
    pass

class Hawk(Preditor):
    pass

class Fish(Preditor, Prey): # Multiple inheritance from fish bigger fish can eat smaller fish 
    pass


rabbit = Rabbit("Nano")
print(rabbit.flee())       # The prey is fleeing

hawk = Hawk("Hawk eye")
print(hawk.hunt())         # The predator is hunting

fish = Fish("Kara")
print(fish.hunt())         # The predator is hunting
print(fish.flee())         # The prey is fleeing
print(fish.eat())
print(fish.name)


print(Fish.__mro__)