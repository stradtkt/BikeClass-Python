class Bike():
  def __init__(self, price, max_speed, miles):
    self.price = price
    self.max_speed = max_speed
    self.miles = miles
  def displayInfo(self, price, max_speed, miles):
    print("This bike costs {}, it has a max speed of {}, and has been ridden for {} miles".format(self.price, self.max_speed, self.miles))
  def ride(self):
    self.total_miles = self.miles + 10
    print("You are riding on the bike, and the end amount of miles is " + self.total_miles)

Bike1 = Bike(20000, 120, 2000)
Bike1.ride()
    