#!/usr/bin/env bash
curl -sw size_download $1
curl -s "$1" | wc -c
