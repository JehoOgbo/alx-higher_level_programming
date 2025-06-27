#!/bin/bash
# sends a get request
curl -sX POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
