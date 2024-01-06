#!/usr/bin/python3
# 6-print_matrix_integer.py
# Bruno Okoth
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            print("{:d}".format(row[col]),
                  end=' ' if col < len(row) - 1 else '')
        print()
