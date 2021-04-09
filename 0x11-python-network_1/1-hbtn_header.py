#!/usr/bin/python3
"""
    request url and print header variable
"""
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.info()
print("{}".format(html['X-Request-Id']))
