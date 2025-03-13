#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""

import sys

def print_stats(total_size, status_counts):
    """Prints the total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

total_size = 0
status_counts = {}
valid_statuses = {200, 301, 400, 401, 403, 404, 405, 500}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 7:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in valid_statuses:
                    status_counts[status_code] = status_counts.get(status_code, 0) + 1
            except ValueError:
                continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
