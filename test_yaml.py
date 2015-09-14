#!/usr/bin/env python
import yaml
import json

from pprint import pprint as pp
my_list = ['one', 'two', 'whatever', 1, 2, 10, {'hostname': 'router', 'ip_address': '10.1.1.12'}]

with open("test_file.yml", "w") as f:
  f.write(yaml.dump(my_list, width=50, indent=4, default_flow_style=False)) 
  f.write(json.dumps(my_list))
