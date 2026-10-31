#!/usr/bin/python3
"""validate the utf8"""


def validUTF8(data):
    """check the data for utf-8 ness"""
    try:
        bytes(data).decode("utf-8")
        return True
    except (ValueError, UnicodeDecodeError):
        return False
