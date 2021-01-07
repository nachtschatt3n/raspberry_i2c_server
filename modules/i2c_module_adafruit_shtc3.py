class Shtc3:
    import board
    import adafruit_shtc3
    def __init__(self, i2c):
      self.interface = self.adafruit_shtc3.SHTC3(i2c)
 
    def print(self):
      print("Temperature: %.2f C" % self.interface.temperature)
      print("Humidity: %0.1f %%fH" % self.interface.relative_humidity)

    def data(self):
      return {
        "temperature" : self.interface.temperature,
        "humidity" : self.interface.relative_humidity,
      }
