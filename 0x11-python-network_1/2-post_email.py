#!/usr/bin/python3
"""
   send a post request
"""
from urllib import request, parse

import sys
data = parse.urlencode({"email": sys.argv[2]})
data = data.encode('ascii')
with request.urlopen(sys.argv[1], data) as response:
    html = response.read()
print(html.decode("utf8"))
