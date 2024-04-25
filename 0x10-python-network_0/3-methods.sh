#!/bin/bash
# brunookoth44@gmail.com
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
