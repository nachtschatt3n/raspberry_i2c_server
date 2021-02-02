class Display:
    import adafruit_ssd1306 as display_driver 
    def __init__(self, i2c):
        self.display = self.display_driver.SSD1306_I2C(128, 32, i2c)
        self.display.fill(0)
        self.display.show()

    def draw(self,sensor):
        self.display.text(sensor.temperature(), 0, 0, 1)
        self.display.text(sensor.humidity(), 0, 10, 1)
        self.display.show()