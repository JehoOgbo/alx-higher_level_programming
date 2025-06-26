#!/bin/bash
# sends a get request
curl -sX GET "$1"
curl -sX POST 'X-School-User-Id=98'
curl -sH "X-School-User-Id: 98" "${1}"
