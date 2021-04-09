#!/usr/bin/python3
"""
    send post request and display body content
"""
import requests
import sys
if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.content.decode('utf8'))
