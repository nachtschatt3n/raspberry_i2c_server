import time
import board
import busio
import adafruit_shtc3
import paho.mqtt.client as mqtt

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

while True:
    print("---------------------")

    print("Temperature: %0.1f C" % sht.temperature)
    client.publish("raspberry_sensors/upstairs/prusa_mini01/temperature", sht.temperature)

    print("Humidity: %0.1f %%fH" % sht.relative_humidity)
    client.publish("raspberry_sensors/upstairs/prusa_mini01/humidity", sht.relative_humidity)

    time.sleep(3)
