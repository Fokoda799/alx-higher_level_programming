#!/usr/bin/python3

if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) != 2:
        q = ""
    else:
        q = sys.argv[1]

    r = requests.post(url, data={'q': q})
    if r.headers['content-type'] == 'application/json':
        try:
            print(f"[{r[id]}] r[name]")
        except Excpetion:
            print("No result")
    else:
        print("Not a valid JSON")
