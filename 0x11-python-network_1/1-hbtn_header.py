#!/usr/bin/python3
""" Response header value """


if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as rep:
        print(rep.headers['X-request-Id'])
