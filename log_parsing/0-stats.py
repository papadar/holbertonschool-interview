#!/usr/bin/python3
import sys

count = 0
result = 0
codes = [0] * 8

try:
    for line in sys.stdin:
        count += 1
        clean_line = line.rstrip('\r\n')
        # print(f"Processing: {clean_line}")
        values = clean_line.split()
        last_item = int(values[-1])
        result += last_item

        code_item = int(values[-2])
        print(f"{code_item}")
        # print(f"last item = {last_item}")
        if count == 10:
            print(f"File size: {result}")
            count = 0

except KeyboardInterrupt:
    print(f"File size: {result}")