class Bh1750:
    import adafruit_bh1750
    def __init__(self, i2c):
      self.interface = self.adafruit_bh1750.BH1750(i2c)

    def print(self):
      print("%.2f Lux" % self.interface.lux)

    def data(self):
      return {
        "lux" : self.interface.lux,
      }