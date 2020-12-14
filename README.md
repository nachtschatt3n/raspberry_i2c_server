sudo chmod 644 /lib/systemd/system/i2c_server.service
sudo systemctl daemon-reload
sudo systemctl enable i2c_server.service


Requirements 
 - Python3
 - pip install busio
 - paho.mqtt
 - Qwicc_py

sudo apt install python3
sudo apt install python3-pip
pip3 install adafruit-circuitpython-lis3dh
pip3 install paho.mqtt
