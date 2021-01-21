#!/usr/bin/python3
"""
script that adds all arguments to a Python list, and then save them to a file:
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        json_l = load_from_json_file("add_item.json")
    except Exception:
        json_l = []

    x = 1
    while (x < len(argv)):
        json_l.append(argv[x])
        x += 1
    save_to_json_file(json_l, "add_item.json")
