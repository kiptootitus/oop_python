class Person:
  def __init__(self, name, address, age, contact_number):
    self.name = name
    self.address = address
    self.age = age
    self.contact_number = contact_number
    
  def greeting(self):
    print(f"Hello, {self.name}")
  
person1 = Person("Titus", "907 kipchoge", 57, +25417649444)
print(person1.address)
person1.greeting()