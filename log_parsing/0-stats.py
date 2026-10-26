#!/usr/bin/python3
import sys

count = 0

try:
    for line in sys.stdin:
        count += 1
        clean_line = line.rstrip('\r\n')
        print(f"Processing: {clean_line}")
        values = clean_line.split()
        if count == 10:
            print("10th line")
            count = 0

except KeyboardInterrupt:
    print("final stats due to interuption")
    
finally:
    print("exiting")