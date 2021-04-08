#!/bin/bash
# display status code
curl -sL -w "%{http_code}" -I -o /dev/null "$1"
