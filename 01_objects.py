#object - is a group of related attributes(variables) and methods(functions)
#       You need a class to create many objects

# Class - a blueprint of used to design the structure and layout of the object.

class Car:
    # constructor
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color 
        self.for_sale = for_sale
        
        
        
car1 = Car("Mustang", 2025, 'Black', False)
print(car1) # this will print the car object memory location
print(car1.model)



# let use methods withing an oblect 

class Trade:
  def __init__(self, currency, lot_size, session, profit, loss):
      self.currency = currency
      self.lot_size = lot_size 
      self.session = session
      self.profit = profit
      self.loss = loss 
     
  def open_trade(self):
    print(f"The trade of {self.currency} was open with lot_size of {self.lot_size} in {self.session} session time")
    
  def take_profit(self):
    return f"Take profit for this amount {self.profit}"
  
  def close_trade(self):
    return f"Close trade when it is in a loss of {self.loss}"
  

trade1 = Trade("EUR/USD", 1.5, "London", 200, 100)

trade1.open_trade()
print(trade1.take_profit())
print(trade1.close_trade())
