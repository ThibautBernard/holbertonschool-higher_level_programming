#!/usr/bin/python3
"""
    request, print header variable
"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if 'X-Request-Id' in r.headers and r:
        print(r.headers['X-Request-Id'])
