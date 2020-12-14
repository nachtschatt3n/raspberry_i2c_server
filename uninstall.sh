sudo service i2c_server stop
sudo systemctl disable i2c_server.service
sudo rm /lib/systemd/system/i2c_server.service
sudo rm /var/log/i2c_server.log
sudo rm -rf /usr/local/lib/i2c_server
sudo systemctl daemon-reload