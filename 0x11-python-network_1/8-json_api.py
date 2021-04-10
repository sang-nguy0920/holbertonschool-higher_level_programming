#!/usr/bin/python3
"""
Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) == 2:
        new = argv[1]
    else:
        new = ""
    fetch = requests.post('http://91cf6a0ab180.b594c0bb.\
                          hbtn-cod.io:5000/search_user', data={'new': new})
    try:
        fetch_dict = fetch.json()
        id = fetch_dict.get('id')
        name = fetch_dict.get('name')
        if len(fetch_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(fetch_dict.get('id'),
                  fetch_dict.get('name')))
    except:
        print("Not a valid JSON")
