#!/usr/bin/python3
"""Module that calculates metrics from HTTP access log entries.

This script reads stdin line by line and computes metrics:
- Input format: "<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>"
- Prints statistics every 10 lines and after a keyboard interruption (CTRL + C)
- Shows total file size and number of lines by status code in ascending order
"""

import sys
import re


def print_stats(total_size, status_codes):
    """Print accumulated statistics.
    
    Args:
        total_size (int): The total file size
        status_codes (dict): Dictionary with status codes and their counts
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0
    
    pattern = r'^\S+ - \[.+\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    
    try:
        for line in sys.stdin:
            line_count += 1
            match = re.match(pattern, line.strip())
            if match:
                status_code = match.group(1)
                file_size = int(match.group(2))
                
                # Update metrics
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            
            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
                
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)
