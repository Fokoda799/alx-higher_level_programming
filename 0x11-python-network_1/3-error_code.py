#!/usr/bin/python3
""" 3. Error code """

if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError
    from sys import argv

    url = argv[1]
    try:
        with urlopen(url) as rep:
            body = rep.read()
        print(body)
    except HTTPError as e:
        print("Error code: ", e.code)
