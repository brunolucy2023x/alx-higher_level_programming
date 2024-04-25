#!/bin/bash 
# brunookoth44@gmail.com
curl -s -L -X HEAD -w "%{http_code}" "$1"
