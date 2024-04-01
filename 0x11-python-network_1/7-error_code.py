#!/usr/bin/python3
""" 7. Error code """

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {} ".format(r.status_code))
