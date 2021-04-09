#!/usr/bin/python3
"""
    send post request and get json response
"""
import requests
import sys
if __name__ == "__main__":
    if sys.argv[1]:
        d = {'q': sys.argv[1]}
    else:
        d = {'q': ''}
    r = requests.post("http://0.0.0.0:5000/search_user", data=d)
    if type(r.json()) == dict:
        if len(r.json()) == 0:
            print('No result')
        else:
            print("[{:d}] {}".format(r.json()['id'], r.json()['name']))
    else:
        print('Not a valid JSON')
