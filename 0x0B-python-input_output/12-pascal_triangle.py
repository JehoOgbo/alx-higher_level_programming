#!/usr/bin/python3
""" forms a pascal triangle with n number of lines """


def pascal_triangle(n):
    """forms a pascal triangle
    Args:

        n: number of lines of the pascal triangle
        Assume n will always be an integer
    """
    if n <= 0:
        return []

    angle = [[1]]
    while len(angle) != n:
        tri = angle[-1] # first case tri = [1, 1]
        temp = [1]
        for i in range(len(tri) - 1): # first case i in range 0 doesnt run
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        angle.append(temp)
    return angle
