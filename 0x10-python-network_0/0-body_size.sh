#!/bin/bash
# 0. cURL body size
curl -sI "$1" | awk '/Content-Length/ {print $2}'
