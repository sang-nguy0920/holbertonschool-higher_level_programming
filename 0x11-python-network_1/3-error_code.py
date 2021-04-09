#!/usr/bin/python3
"""
Write a Python script that takes in a URL,
sends a request to the URL and displays the
body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import urllib.error as error
    import urllib.request as request
    from sys import argv
    url_req = request.Request(argv[1])
    try:
        with request.urlopen(url_req) as req:
            print(req.read().decode('utf-8'))
    except error.HTTPError as erroneous:
        print("Error code: {}".format(erroneous.code))
