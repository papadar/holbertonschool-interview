#!/usr/bin/python3
"""the lockbox documentation"""


def canUnlockAll(boxes):
    """vars"""
    count = len(boxes)
    boxop = [0] * count
    boxop[0] = 1

    """
    cycle through each box, & mark the unlocked boxes
    repeat if a new key was found
    """
    again = True
    while again:
        again = False
        for i in range(count):
            if boxop[i] == 1:
                for value in boxes[i]:
                    if (boxop[value] == 0):
                        boxop[value] = 1
                        again = True

    """true if the sum of unlocked boxes equals the count"""
    if sum(boxop) == count:
        return True
    else:
        return False
