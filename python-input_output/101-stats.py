#!/usr/bin/python3
"""Module that calculates metrics from HTTP access log entries.

This script reads stdin line by line and computes metrics:
- Input format: "<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
  <status code> <file size>"
- Prints statistics every 10 lines and after a keyboard interruption (CTRL + C)
- Shows total file size and number of lines by status code in ascending order
"""

import sys
import signal


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption."""
    print_stats(total_size, status_codes)
    sys.exit(0)


# Register signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Initialize variables
total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            # Split the line by spaces
            parts = line.split()

            # Make sure we have enough parts to analyze
            if len(parts) >= 7:
                # Status code should be the 8th element from the end
                status_code = parts[-2]

                # File size should be the last element
                file_size = int(parts[-1])

                # Update metrics
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            # Increment count regardless of parsing success
            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        except (IndexError, ValueError):
            # Continue even if we can't parse a line
            continue

    # Print final stats if not a multiple of 10
    if line_count % 10 != 0:
        print_stats(total_size, status_codes)

except KeyboardInterrupt:
    # This will be caught by the signal handler
    pass
