# Abstract Class - A class that  cannot be instantiated on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared  but have  no implementation

from abc import ABC, abstractmethod
from math import pi
class Vehicle(ABC):
  def __init__(self):
    pass
  @abstractmethod
  def go(self):
    pass
  
  @abstractmethod
  def stop(self):
    pass
  

class Car(Vehicle):
  def __init__(self):
    super().__init__()

  def go(self):
      print("The car is moving.")

  def stop(self):
      print("The car has stopped.")

car = Car()
car.go()



# super class

class Shape(ABC):
  def __init__(self, color, is_filled):
    self.color = color
    self.is_filled = is_filled
    
  @abstractmethod
  def area(self):
    pass

class Circle(Shape):
  def __init__(self, color, is_filled, radius):
    super().__init__(color, is_filled)
    self.radius = radius
  def __str__(self):
    return f"Circle(color={self.color}, filled={self.is_filled}, radius={self.radius})"
  
  def area(self):
    return pi * self.radius

class Rectangle(Shape):
  def __init__(self, color, is_filled, width, height):
    super().__init__(color, is_filled)
    self.width = width
    self.height = height
  
  def area(self):
    return self.width * self.height
    
    

circle = Circle(color="blue", is_filled=True, radius=5)

rect = Rectangle(color="Yellow", is_filled=True, width=10, height=5)

print(rect)
print(rect.area())
print(circle.area())