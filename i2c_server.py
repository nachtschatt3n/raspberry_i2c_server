import time
import board
import busio
import yaml
import pry

from modules import *

from i2c_server_mqtt import *

with open("/etc/i2c_server/i2c_server.conf.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

i2c = busio.I2C(board.SCL, board.SDA)
mqtt_cient = MqttClient(cfg["mqtt"])
i2c_sensors = {}

for sensor in cfg["modules"]:
   #print(sensor)
    #pry()
    constructor = globals()[sensor]
    i2c_sensors[sensor.lower()] = constructor(i2c)

while True:
  for i2c_sensor in i2c_sensors:
    sensor = i2c_sensors[i2c_sensor]
    mqtt_cient.publish(sensor.data())
    sensor.print()
    time.sleep(3)

#test1
