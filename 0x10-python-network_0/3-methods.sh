#!/bin/bash
# print the methods allowed by the server
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-
