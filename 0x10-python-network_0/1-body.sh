#!/bin/bash
# display body content if 200 status code
status_code=$(curl -sL -w "%{http_code}" -I "$1" -o /dev/null)
if [[ "$status_code" -eq 200 ]]
then
    curl -Ls "$1"
fi
