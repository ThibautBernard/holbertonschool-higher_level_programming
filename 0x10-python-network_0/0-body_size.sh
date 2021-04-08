#!/bin/bash
# display content length
curl -sI $1 | grep -e Content-Length | cut -d: -f2
