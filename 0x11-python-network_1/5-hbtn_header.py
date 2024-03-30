#!/usr/bin/python3
""" 5. Response header value """

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    id = r.headers['X-Request-Id']
    print(id)
