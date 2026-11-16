#!/usr/bin/python3
"""ths is the documentation text"""
import math


def makeChange(coins: list, value) -> int:
    """calculate the smallest number of coins"""

    if value <= 0:
        return 0
    """sort the coins list largest to smallest"""
    scoins = sorted(coins, reverse=True)
    count = 0

    """check each coin can fit into value"""
    for coin in scoins:
        """print(f"coin is {coin} & value remaining is {value}")"""
        while coin <= value:
            count += 1
            value = value - coin
            if value == 0:
                return count

    return -1
