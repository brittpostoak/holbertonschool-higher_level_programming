#!/usr/bin/python3
"""
Returns list of lists of integers representing Pascal’s triangle.
"""


def pascal_triangle(n):
    """Begins function - pascal traingle"""
    pascal_triangle = []
    previous = [1]
    if n <= 0:
        return pascal_triangle
    for row_number in range(n):
        rowlist = []
        if row_number == 0:
            rowlist = [1]
        else:
            for i in range(row_number + 1):
                if i == 0:
                    rowlist.append(0 + previous[i])
                elif i == (row_number):
                    rowlist.append(previous[i - 1] + 0)
                else:
                    rowlist.append(previous[i - 1] + previous[i])
        previous = rowlist
        pascal_triangle.append(rowlist)
    return pascal_triangle
