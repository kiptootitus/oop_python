from datetime import datetime

class Dog:
  def __init__(self, name, breed, owner):
    self.name= name
    self.breed=breed
    self.owner=owner
    
  def what_kind_of_the_dog(self):
    print(f"The breed of {self.name} is {self.breed}")
    
    
class Owner:
  def __init__(self, name, contact_number, email):
    self.name = name
    self._email=email
    self.contact_number=contact_number
    
  def get_email(self):
    print(f"This email {self._email} was access at {datetime.now()}") 
    return self._email
          
owner1=Owner("Titus", +2540100506258,"kip@gmail.com ")
dog1 = Dog("Bosco", "german shepherd", owner1)
print(owner1.get_email())
print(dog1.owner.name)