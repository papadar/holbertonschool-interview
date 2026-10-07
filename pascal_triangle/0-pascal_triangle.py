#!/usr/bin/python3
def pascal_triangle(n):
    count = 0
    tri = [[1]]

    if (n <= 0):
        return []

    while (count < n):
        pre = tri[-1]
        row = [1]
        for i in range(len(pre) - 1):
            row.append(pre[i] + pre[i + 1])
        row.append(1)
        tri.append(row)
        count += 1

    return tri
