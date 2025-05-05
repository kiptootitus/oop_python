# Abstract Class - A class that  cannot be instantiated on its own; Meant to be subclassed.
#                 They can contain abstract methods, which are declared  but have  no implementation

from abc import ABC, abstractmethod

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
