class Lps2x:
    import adafruit_lps2x
    def __init__(self, i2c):
      self.interface = self.adafruit_lps2x.LPS22(i2c)

    def print(self):
      print("Temperature: %.2f C" % self.interface.temperature)
      print("Pressure: %.2f hPa" % self.interface.pressure)

    def data(self):
      return {
        "temperature" : self.interface.temperature,
        "pressure": self.interface.pressure
      }
