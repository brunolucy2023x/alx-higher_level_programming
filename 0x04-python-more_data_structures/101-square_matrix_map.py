#!/usr/bin/python3
# 101-square_matrix_map.py
# Bruno Okoth
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda i: i ** 2, row)), matrix))
