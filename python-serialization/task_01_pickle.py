#!/usr/bin/env python3

import pickle
"""Learn how to serialize and deserialize custom Python
objects using the pickle module."""

class CustomObject:
    def __init__(self, name, age, is_student):
        "attributes for custom object"
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        "printing method "
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        "convert data to pickle"
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except OSError:
            return None

    @classmethod
    def deserialize(cls, filename):
        "converts back to original data structure "
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except OSError:
            return None
