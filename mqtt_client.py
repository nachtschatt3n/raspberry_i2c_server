class MqttClient:
    import paho.mqtt.client as mqtt

    def __init__(self, cfg):
      self.room = cfg["room"]
      self.name = cfg["name"]        
      self.client = self.mqtt.Client()
      self.client.on_connect = self.on_connect
      self.client.on_disconnect = self.on_disconnect
      self.client.connect(cfg["host"], cfg["port"], 60)
      self.client.loop_start()

    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_disconnect(self,client, userdata, rc):
        if rc != 0:
            print("Unexpected disconnection.")

    def publish(self,sensor_data):
        for sensor_name in sensor_data:
            sensor_value = sensor_data[sensor_name]
            mqtt_path = "i2c/" + self.room + "/" + self.name + "/" + sensor_name
            self.client.publish(mqtt_path, sensor_value)