import time
import board
import busio

from i2c_module_adafruit_shtc3 import Shtc3
from i2c_module_adafruit_pct2075 import Pct2075
from i2c_module_adafruit_pct2075 import Lps2x
from i2c_module_adafruit_bh1750 import Bh1750
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
  foreach(module):
    mqtt_cient.publish(module.sensor_data)
    module.print()
    time.sleep(3)
