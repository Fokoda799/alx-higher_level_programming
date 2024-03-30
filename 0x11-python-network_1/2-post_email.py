#!/usr/bin/python3
""" 2. POST an email """

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    email = urlencode({'email': argv[2]})
    email = email.encode('ascii')
    req = Request(url, email)
    with urlopen(req) as rep:
        body = rep.read()
    print(body.decode('utf-8'))
