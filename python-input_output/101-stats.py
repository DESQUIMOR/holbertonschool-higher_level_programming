#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics.
Calculates total file size and counts occurrences of HTTP status codes.
Prints stats every 10 lines and handles keyboard interruptions.
"""
import sys
import re

def print_stats(total_size, status_codes):
    """Print the accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys(), key=int):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Initialize variables
total_size = 0
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0, 
    '403': 0, '404': 0, '405': 0, '500': 0
}
line_count = 0

# Regular expression pattern for parsing log lines
log_pattern = r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'

try:
    for line in sys.stdin:
        try:
            # Parse the line using regex
            match = re.match(log_pattern, line.strip())
            if match:
                status_code = match.group(1)
                file_size = int(match.group(2))
                
                # Update metrics
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                # Increment line count
                line_count += 1
                
                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
        except Exception:
            # Skip lines that don't match the expected format
            pass
                
except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats(total_size, status_codes)
    sys.exit(0)

# Print stats at the end if there are lines processed but not a multiple of 10
if line_count > 0 and line_count % 10 != 0:
    print_stats(total_size, status_codes)
