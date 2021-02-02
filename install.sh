# create conf dir
sudo mkdir /etc/i2c_server

# create lib dir
sudo mkdir /usr/local/lib/i2c_server

# create log
sudo touch /var/log/i2c_server.log

#copy files
sudo cp i2c_server.conf.yaml /etc/i2c_server
sudo cp -R * /usr/local/lib/i2c_server

# prepare the systemd service and autostart
sudo cp i2c_server.service /lib/systemd/system/i2c_server.service
sudo systemctl daemon-reload
sudo systemctl enable i2c_server.service
sudo service i2c_server start