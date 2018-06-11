class Bike(object):
  def __init__(self, price, max_speed, miles):
    self.price = price
    self.max_speed = max_speed
    self.miles = miles


  def display_info(self):
    print "Price: " + str(self.price)
    print "Max speed: " + str(self.max_speed)
    print "Miles: " + str(self.miles)

  def ride(self):
    print "Riding"
    self.miles += 10
    return self.miles

  def reverse(self):
    print "Reversing"
    self.miles -= 5
    return self.miles
bike_1 = Bike(2000, 120, 10000)
bike_2 = Bike(1000, 100, 5500)
print "Bike 1"
bike_1.ride()
bike_1.ride()
bike_1.ride()
bike_1.reverse()
bike_1.display_info()
print '\n'
print "Bike 2"
bike_2.ride()
bike_2.ride()
bike_2.reverse()
bike_2.reverse()
bike_2.display_info()