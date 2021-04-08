#!/bin/bash
# display allow http method avalaible
curl -sI -L "$1" | grep Allow | cut -d ' ' -f2,3,4,5,6
