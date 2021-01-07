class Ssd1306:
    import board  
    import adafruit_ssd1306

    def __init__(self, i2c):
      self.interface = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

    def draw(text):
      self.interface.fill(0)
      self.interface.show()
      self.interface.text(text, 0, 0)
      self.interface.show()
