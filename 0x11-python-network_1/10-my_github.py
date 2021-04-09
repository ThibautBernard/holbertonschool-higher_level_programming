#!/usr/bin/python3
"""
    fetch api github about an user
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) == 3:
        h = {'Accept': 'application/vnd.github.v3+json'}
        u = "https://api.github.com/users/{}".format(sys.argv[1])
        r = requests.get(u, headers=h)
        if 'id' in r.json():
            print(r.json()['id'])
        else:
            print('None')
    else:
        print('None')
