#!/usr/bin/python3
"""
Log Metrics Script

This script reads stdin line by line and computes HTTP request metrics.
It prints the total file size and counts occurrences of specific HTTP status codes.
Statistics are displayed every 10 lines and upon termination via KeyboardInterrupt (CTRL + C).

Expected input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Example Output:
File size: <total size>
<status code>: <number>

Only valid HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500) are counted.
"""

import sys

def print_info():
    """Prints the total file size and status code counts."""
    print('File size: {:d}'.format(file_size))
    for scode, code_times in sorted(status_codes.items()):
        if code_times > 0:
            print('{}: {:d}'.format(scode, code_times))

# Dictionary to store status code counts
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

lc = 0  # Line counter
file_size = 0  # Total file size accumulator

try:
    for line in sys.stdin:
        if lc != 0 and lc % 10 == 0:
            print_info()
        
        pieces = line.split()
        
        try:
            status = int(pieces[-2])
            if str(status) in status_codes:
                status_codes[str(status)] += 1
        except (IndexError, ValueError):
            pass
        
        try:
            file_size += int(pieces[-1])
        except (IndexError, ValueError):
            pass
        
        lc += 1
    
    print_info()
except KeyboardInterrupt:
    print_info()
    raise
