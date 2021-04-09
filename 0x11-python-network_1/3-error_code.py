#!/usr/bin/python3
"""
    request, print body or catch error
"""
from urllib import request, parse, error

import sys
try:
    with request.urlopen(sys.argv[1]) as response:
            html = response.read()
    print(html.decode('utf8'))
except error.HTTPError as err:
    print("Error code: {}".format(err.code))
