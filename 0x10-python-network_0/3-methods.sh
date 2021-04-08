#!/bin/bash
# display allow http method avalaible
curl -sI -L -X "$1" | grep Allow | cut -d: -f2
