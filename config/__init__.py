import yaml

import os

filepath = os.path.join(os.path.dirname(__file__), 'configdata.yaml')
with open(filepath) as f:
    configdata = yaml.safe_load(f)
    print(configdata)
