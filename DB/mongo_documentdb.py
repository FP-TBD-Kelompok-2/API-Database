#!/usr/bin/env python
import yaml
from flask import jsonify

with open("./app.yaml", "r") as stream:
    try:
        env = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


HOST_URI = str(env["env_variables"]["HOST_URI"])
print('gegeg')