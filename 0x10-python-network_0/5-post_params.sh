#!/bin/bash
# display body content and send a post request with variables in url
curl -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
