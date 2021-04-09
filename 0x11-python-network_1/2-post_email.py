#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the
email as a parameter, and displays the body of the
response (decoded in utf-8)
"""


if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    v = {'email': argv[2]}
    d = parse.urlencode(v).encode('utf-8')
    url_req = request.Request(argv[1], d)
    with request.urlopen(url_req) as req:
        print(req.read().decode('utf-8'))
