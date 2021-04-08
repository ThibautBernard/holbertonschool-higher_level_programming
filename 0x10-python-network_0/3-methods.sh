#!/bin/bash
# display allow http method avalaible
curl -sL -w "%{allow}" -I -o /dev/null "$1"
# curl -sI -L -X "$1" | grep Allow | cut -d: -f2
