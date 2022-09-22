#!/bin/bash
# Make request and display response
curl -sI "$1" | grep "content-length" | cut -d '' -f 2
