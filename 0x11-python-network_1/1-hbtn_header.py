#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    url_req = request.Request(argv[1])
    with request.urlopen(url_req) as req:
        print(req.headers.get('X-Request-Id'))
