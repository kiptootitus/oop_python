class User:
  def __init__(self, username, email):
    self.username = username
    self._email = email
    
  # setting a getter property in python  
  @property
  def email(self):
    print("Email accessed")
    return self._email
  
  @email.setter
  def email(self, new_email):
    # validate
    if '@' in new_email:
      self._email = new_email
  
user1 = User("dev.sudo", "dev.sudo.titus@gmail.com")
user1.email=("titus@gmail.com")
print(user1.email)

