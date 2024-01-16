#!/usr/bin/python3
"""Load, add, save"""

import json
import sys
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file

pyList = sys.argv[1:]
filename = "add_item.json"
try:
    jsonList = load(filename)
    for arg in pyList:
        jsonList.append(arg)
    save(jsonList, filename)
except Exception as e:
    save(pyList, filename)
