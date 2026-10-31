#!/usr/bin/python3
"""validate the utf8 one value at a time"""


def validUTF8(data):
    """check the data for utf-8 ness"""
    remaining = 0

    for num in data:
        """check each byte"""
        byte = num & 0xFF

        if remaining == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                remaining = 1
            elif byte >> 4 == 0b1110:
                remaining = 2
            elif byte >> 3 == 0b11110:
                remaining = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining -= 1

    return remaining == 0
