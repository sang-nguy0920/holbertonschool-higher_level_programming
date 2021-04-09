#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    fetch = requests.get('https://intranet.hbtn.io/status')
    fetch_text = fetch.text
    print("Body response:")
    print("\t- type: {}".format(type(fetch_text)))
    print("\t- content: {}".format(fetch_text))
