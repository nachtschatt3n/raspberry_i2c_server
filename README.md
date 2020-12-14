sudo chmod 644 /lib/systemd/system/i2c_server.service
sudo systemctl daemon-reload
sudo systemctl enable i2c_server.service


Requirements 
 - Python3
 - pip install busio
 - paho.mqtt
 - Qwicc_py
 