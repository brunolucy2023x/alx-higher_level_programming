#!/usr/bin/python3
# 3-infinite_add.py
# Bruno Okoth
if __name__ == "__main__":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            result += int(arg)
    print(result)
