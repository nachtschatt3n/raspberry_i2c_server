import sys
import time
import board
import busio
import yaml
import pry

from modules import *
from i2c_server_mqtt import *

# set logging to var log
log_file = open("/var/log/i2c_server.log","w")
sys.stdout = log_file

# load config 
with open("/etc/i2c_server/i2c_server.conf.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

# init i2c 
i2c = busio.I2C(board.SCL, board.SDA)
i2c_sensors = {}

for sensor in cfg["modules"]:
    constructor = globals()[sensor]
    i2c_sensors[sensor.lower()] = constructor(i2c)

display = Shtc3(i2c)

#init mqtt
mqtt_cient = MqttClient(cfg["mqtt"])

#main loop
while True:
  for i2c_sensor in i2c_sensors:
    sensor = i2c_sensors[i2c_sensor]
    mqtt_cient.publish(sensor.data())
    if cfg["log"] == "true":
      sensor.print()
    display.draw('test')
    time.sleep(3)