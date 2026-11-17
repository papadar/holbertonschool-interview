#!/usr/bin/python3
"""ths is the documentation text"""


def makeChange(coins: list, value) -> int:
    """calculate the smallest number of coins"""

    """various type checks to prevent attempting impossible solutions"""
    if value <= 0:
        return 0

    if not isinstance(value, int) or isinstance(value, bool):
        return -1

    for coin in coins:
        if not isinstance(coin, int) or isinstance(coin, bool):
            return -1

    if any(coin < 0 for coin in coins):
        return -1

    if len(coins) < 1:
        return -1
    
    """sort the coins list largest to smallest"""
    scoins = sorted(coins, reverse=True)
    smallest = 0

    #print(scoins)

    """try with a single coin ommitted"""
    for i in range (len(scoins)+1):
        count = 0
        check = value
        tscoins = scoins[:i] + scoins[i + 1:]
        #print(tscoins) 
        #print(value)

        """check each coin can fit into value"""
        for coin in tscoins:
            #print(f"coin is {coin} & value remaining is {value}")
            while coin <= check:
                count += 1
                #print(f"count with coins{tscoins} is {count}")
                check = check - coin
                if check == 0:
                    if smallest == 0 or smallest > count:
                        smallest = count 
                        #print("value is zero")

    if smallest != 0:
        return smallest
    
    return -1
