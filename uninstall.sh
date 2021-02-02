# try to stop the service
sudo service i2c_server stop
sudo systemctl disable i2c_server.service

# remove the files
sudo rm /lib/systemd/system/i2c_server.service
sudo rm /var/log/i2c_server.log
sudo rm -rf /usr/local/lib/i2c_server
sudo rm -rf /etc/i2c_server

#cleanup startup daemons
sudo systemctl daemon-reload