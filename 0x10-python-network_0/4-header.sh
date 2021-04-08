#!/bin/bash
# display body response and send get requrest with header
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
