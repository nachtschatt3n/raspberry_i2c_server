import yaml
from test_yaml_2 import myTest

with open("i2c_server.conf.yaml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

for section in cfg["modules"]:
    print(section)
print(cfg["mqtt"]["host"])

x = myTest('Huhu')
x.dodo()
