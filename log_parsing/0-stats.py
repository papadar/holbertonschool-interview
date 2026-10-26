#!/usr/bin/python3
"""read the log stdout"""
import sys

count = 0
result = 0
codes = [0] * 8
names = [200, 301, 400, 401, 403, 404, 405, 500]


def code_count(code: int):
    """count the codes"""
    match code:
        case 200:
            codes[0] += 1
        case 301:
            codes[1] += 1
        case 400:
            codes[2] += 1
        case 401:
            codes[3] += 1
        case 403:
            codes[4] += 1
        case 404:
            codes[5] += 1
        case 405:
            codes[6] += 1
        case 500:
            codes[7] += 1


def print_codes():
    """print the code tally"""
    for i, value in enumerate(codes):
        if value > 0:
            print(f"{names[i]}: {value}")


try:
    """try to read ther stdout"""
    for line in sys.stdin:
        count += 1
        clean_line = line.rstrip('\r\n')
        # print(f"Processing: {clean_line}")
        values = clean_line.split()
        last_item = int(values[-1])
        result += last_item
        code_item = int(values[-2])
        code_count(code_item)
        # print(f"{code_item}")
        # print(f"last item = {last_item}")
        if count == 10:
            """print stats every 10 logs"""
            print(f"File size: {result}")
            print_codes()
            count = 0

except KeyboardInterrupt:
    """if user quits, print stats"""
    print(f"File size: {result}")
    print_codes()
