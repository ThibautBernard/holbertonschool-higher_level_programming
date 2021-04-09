#!/usr/bin/python3
"""
    fetch api github about an user
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) == 3:
        h = {'Accept': 'application/vnd.github.v3+json'}
        u = "https://api.github.com/user"
        r = requests.get(u, auth=(sys.argv[1], sys.argv[2]), headers=h)
        if 'id' in r.json():
            print(r.json()['id'])
        else:
            print('None')
    else:
        print('None')
