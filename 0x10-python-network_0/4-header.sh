#!/bin/bash
# display body response and send get requrest with header
curl -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
