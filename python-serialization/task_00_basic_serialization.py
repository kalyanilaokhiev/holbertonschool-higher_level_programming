#!/usr/bin/env python3
import json
"""Create a basic serialization module that adds the functionality to serialize
a Python dictionary to a JSON file and deserialize the JSON
file to recreate the Python Dictionary."""


def serialize_and_save_to_file(data, filename):
    """saves json file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """returns a python dictionary wih deserialized json data from file"""
    with open(filename, "r", encoding="utf-8") as f:
        json.dump(f)
