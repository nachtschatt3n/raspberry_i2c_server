class MqttClient:
    import paho.mqtt.client as mqtt
    
    def __init__(self, cfg):
      self.client = self.mqtt.Client()
      self.client.on_connect = self.on_connect
      self.client.on_disconnect = self.on_disconnect
      self.client.connect("192.168.40.211", 1883, 60)
      self.client.loop_start()

    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")

    def publish(sensor_data)
        pry()