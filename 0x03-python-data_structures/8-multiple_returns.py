#!/usr/bin/python3
# 8-multiple_returns.py
# Bruno Okoth
def multiple_returns(sentence):
    return len(sentence), sentence[0] if sentence else None
