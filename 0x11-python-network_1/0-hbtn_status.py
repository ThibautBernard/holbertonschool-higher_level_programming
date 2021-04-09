#!/usr/bin/python3
"""
    request url and print his value, type, utf8 content
"""
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
print("Body response:")
print("    - type: {}".format(type(html)))
print("    - content: {}".format(html))
print("    - utf8 content: {}".format(html.decode('utf8')))