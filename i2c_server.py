import sys
import time
import board
import busio
import yaml
import pry

from sensors import *
from displays import * 
from mqtt_client import *

# set logging to var log
log_file = open("/var/log/i2c_server.log","w")
sys.stdout = log_file

# load config 
with open("/etc/i2c_server/i2c_server.conf.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

# init i2c 
i2c = busio.I2C(board.SCL, board.SDA)
i2c_sensors = {}
i2c_displays ={}

#load the sensor modules
for sensor in cfg["sensors"]:
    constructor = globals()[sensor]
    i2c_sensors[sensor.lower()] = constructor(i2c)

#init displays
for display in cfg["displays"]:
    constructor = globals()[display]
    i2c_displays[sensor.lower()] = constructor(i2c)

#init mqtt
mqtt_cient = MqttClient(cfg["mqtt"])

#main loop
while True:
  for i2c_sensor in i2c_sensors:
    sensor = i2c_sensors[i2c_sensor]
    mqtt_cient.publish(sensor.data())
    #if cfg["log"] == "true":
      #sensor.print()
    for i2c_display in i2c_displays:
      i2c_display.draw()
    time.sleep(3)