#!/usr/bin/python3

"""function to multipy matrices"""


def matrix_mul(m_a, m_b):
    """multiply the two argument as matrices
    Args:
        m_a: list of lists containing ints or floats
        m_b: list of lists containing ints or floats
    Doctests contained in tests/100-matrix_mul.txt
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    i = 0
    check = 0
    lengtha = len(m_a)
    while i < lengtha:
        if type(m_a[i]) is not list:
            raise TypeError("m_a must be a list of lists")
        check = 1
        i += 1
    i = 0
    lengthb = len(m_b)
    while i < lengthb:
        if type(m_b[i]) is not list:
            raise TypeError("m_b must be a list of lists")
        check = 2
        i += 1
    if lengtha == 0:
        raise ValueError("m_a can't be empty")
    if lengtha == 1:
        if len(m_a[0]) == 0:
            raise ValueError("m_a can't be empty")
    if lengthb == 0:
        raise ValueError("m_b can't be empty")
    if lengthb == 1:
        if len(m_b[0]) == 0:
            raise ValueError("m_b can't be empty")
    for liste in m_a:
        for element in liste:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for liste in m_b:
        for element in liste:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    check1a = len(m_a[0])
    for ele in m_a:
        if check1a != len(ele):
            raise TypeError("each row of m_a must be of the same size")
        check1a = len(ele)
    check1 = len(m_b[0])
    for els in m_b:
        if check1 != len(els):
            raise TypeError("each row of m_b must be of the same size")
        check1 = len(els)
    if check1a != lengthb:
        raise ValueError("m_a and m_b can't be multiplied")
    # Error checking done writing actaul multiplication function
    # return np.dot(m_a, m_b)
    result = []  # create list which will be adequate
    for x in range(lengtha):
        result.append([])  # append an empty list number of row times

        for y in range(len(m_b[0])):
            result[x].append(0)  # append a number to make up for the columns
    num = 0
    for a in range(lengtha):
        for j in range(len(m_b[0])):
            for k in range(lengthb):
                result[a][j] += m_a[a][k] * m_b[k][j]
    return result
