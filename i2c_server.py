import time
import board
import busio

from .active_modules/* import *
from i2c_server_mqtt import MqttClient

with open("/etc/i2c_server/i2c_server.conf.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

i2c = busio.I2C(board.SCL, board.SDA)
mqtt_cient = MqttClient(cfg["mqtt"])
i2c_sensors = {}

for sensor in cfg["active_sensors"]:
    constructor = globals()[sensor]
    i2c_sensors[sensor.lower()] = constructor()

while True:
  for sensor in i2c_sensors:
    mqtt_cient.publish(sensor.data)
    sensor.print()
    time.sleep(3)
