#!/usr/bin/python3
""" Pascals Triangle that return list """


def pascal_triangle(n):
    """implementing pascal triangle"""

    if n <= 0:
        return []
    

    p_triangle = [[1]]

    for angle in range(1, n):
        tri_row = [1]
        for _ in range(1, len(p_triangle[-1])):
            tri_row.append(p_triangle[-1][_-1] + p_triangle[-1][_])
        tri_row.append(1)
        p_triangle.append(tri_row)
    return p_triangle