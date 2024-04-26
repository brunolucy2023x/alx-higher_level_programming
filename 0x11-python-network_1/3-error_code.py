#!/usr/bin/python3
"""
brunookoth44@gmail.com
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            response_text = response.read().decode("utf-8")
            print(response_text)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
