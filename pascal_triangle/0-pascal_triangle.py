#!/usr/bin/python3
"""the pascal triangle documentation"""


def pascal_triangle(n):
    """count and list of lists"""
    count = 0
    tri = [[1]]

    """edge case - zero returns a zero length list"""
    if (n <= 0):
        return []

    """cycle through the count, and build each row one value at a time"""
    while (count < n):
        pre = tri[-1]
        row = [1]
        for i in range(len(pre) - 1):
            row.append(pre[i] + pre[i + 1])
        row.append(1)
        tri.append(row)
        count += 1

    return tri
