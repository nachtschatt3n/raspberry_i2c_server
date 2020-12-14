# Updater

#make sure the service is stopped
sudo service i2c_server stop

#bin files
sudo rm -rf /usr/local/lib/i2c_server
sudo cp -R * /usr/local/lib/i2c_server

#config files
sudo cp i2c_server.conf.yaml /etc/i2c_server
sudo cp -R * /usr/local/lib/i2c_server

#system service
sudo rm /lib/systemd/system/i2c_server.service
sudo cp i2c_server.service /lib/systemd/system/i2c_server.service
sudo systemctl daemon-reload
sudo service i2c_server start
