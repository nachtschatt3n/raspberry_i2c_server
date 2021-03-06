class Pct2075:
    import board
    import adafruit_pct2075
    def __init__(self, i2c):
      self.interface = self.adafruit_pct2075.PCT2075(i2c)

    def print(self):
      print("Temperature: %.2f C" % self.interface.temperature)

    def temperature(self):
      return "Temperature: %.2f C" % self.interface.temperature

    def data(self):
      return {
        "temperature" : self.interface.temperature
      }
