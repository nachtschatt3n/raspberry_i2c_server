sudo touch /etc/i2c_server
sudo mkdir /usr/local/lib/i2c_server
sudo touch /var/log/i2c_server.log
sudo copy i2c_server.conf.yaml /etc/i2c_server
sudo copy i2c_server.py /usr/local/lib/i2c_server
sudo copy i2c_server.service /lib/systemd/system/i2c_server.service
sudo systemctl daemon-reload
sudo systemctl enable i2c_server.service
sudo service i2c_server start