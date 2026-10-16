#!/usr/bin/env python3
import csv
import json
"""reading data from one format (CSV) and converting it
into another format (JSON) using serialization techniques."""


def convert_csv_to_json(filename):
    """converts csv to json"""
    try:
        data = []
        # convert each row into a dictionary
        with open(filename, "r", encoding="utf-8") as csv_file:
            read = csv.DictReader(csv_file)
            for i in read:
                data.append(i)

        # serialize the list of dictionaries using the json module.
        with open('data.json', "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except OSError:
        return False
