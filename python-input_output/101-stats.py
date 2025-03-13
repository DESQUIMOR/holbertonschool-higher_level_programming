#!/usr/bin/python3
"""
Log Metrics Script

This script reads stdin line by line and computes metrics for HTTP request logs.
It prints statistics every 10 lines and on a keyboard interruption (CTRL + C).

Expected input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Example Output:
File size: <total size>
<status code>: <number>

Only valid HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500) are counted.
"""

import sys

def print_stats(total_size, status_counts):
    """Prints the total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

def process_line(line, total_size, status_counts, valid_statuses):
    """Processes a single log line and updates metrics."""
    parts = line.split()
    if len(parts) >= 7:
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_size += file_size
            if status_code in valid_statuses:
                status_counts[status_code] = status_counts.get(status_code, 0) + 1
        except ValueError:
            pass
    return total_size

def main():
    """Main function to read stdin and compute metrics."""
    total_size = 0
    status_counts = {}
    valid_statuses = {200, 301, 400, 401, 403, 404, 405, 500}
    line_count = 0
    
    try:
        for line in sys.stdin:
            total_size = process_line(line.strip(), total_size, status_counts, valid_statuses)
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)
        print_stats(total_size, status_counts)
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

if __name__ == "__main__":
    main()
