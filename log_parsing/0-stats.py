#!/usr/bin/python3
"""Log parsing: reads stdin and prints file size and status code stats."""
import re
import sys

PATTERN = re.compile(
    r'^\S+ - \[[^\]]*\] "GET /projects/260 HTTP/1\.1" (\S+) (\d+)$'
)
VALID_CODES = (200, 301, 400, 401, 403, 404, 405, 500)


def print_stats(total_size, counts):
    """Print total file size and per-status-code line counts."""
    print("File size: {}".format(total_size))
    for code in sorted(counts):
        print("{}: {}".format(code, counts[code]))


def main():
    """Read stdin line by line and print stats every 10 lines."""
    total_size = 0
    counts = {}
    lines = 0
    try:
        for line in sys.stdin:
            match = PATTERN.match(line.rstrip("\r\n"))
            if not match:
                continue
            total_size += int(match.group(2))
            try:
                code = int(match.group(1))
            except ValueError:
                code = None
            if code in VALID_CODES:
                counts[code] = counts.get(code, 0) + 1
            lines += 1
            if lines % 10 == 0:
                print_stats(total_size, counts)
    finally:
        print_stats(total_size, counts)


if __name__ == "__main__":
    main()
