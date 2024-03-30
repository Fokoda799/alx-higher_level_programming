#!/usr/bin/python3
""" 0. What's my status? """


if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen('https://alx-intranet.hbtn.io/status') as rep:
        status = rep.read()
    print("Body response: ")
    print(f"\t- type: {type(status)}")
    print("\t- content: ", status)
    print("\t- utf8 content: ", status.decode('utf-8'))
