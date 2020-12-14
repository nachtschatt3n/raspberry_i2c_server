import time
import board
import busio
import paho.mqtt.client as mqtt

from i2c_module_adafruit_pct2075 import pct2075
from i2c_module_adafruit_shtc3 import shtc3
from i2c_module_adafruit_pct2075 import lps2x
from i2c_module_adafruit_bh1750 import bh1750


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.connect("192.168.40.211", 1883, 60)
client.loop_start()

i2c = busio.I2C(board.SCL, board.SDA)
sht = adafruit_shtc3.SHTC3(i2c)
pct = 
lps = 
bh1750 = adafruit_bh1750.BH1750(i2c)

while True:
    print("---------------------")


    print("SHT Temperature: %0.1f C" % sht.temperature)
    client.publish("raspberry_sensors/living_room/sht_temperature", sht.temperature)

    print("LPS Temperature: %.2f C" % lps.temperature)
    client.publish("raspberry_sensors/living_room/lps_temperature", lps.temperature)

    print("Humidity: %0.1f %%fH" % sht.relative_humidity)
    client.publish("raspberry_sensors/living_room/humidity", sht.relative_humidity)

    
    client.publish("raspberry_sensors/living_room/pressure", lps.pressure)

    print("%.2f Lux" % bh1750.lux)
    client.publish("raspberry_sensors/living_room/lux", bh1750.lux)

    time.sleep(3)
