#!/usr/bin/python3
"""Module that calculates metrics from HTTP access log entries.

This script reads stdin line by line and computes metrics:
- Input format: "<IP Address> - [<date>]"
- Prints statistics every 10 lines and after a keyboard interruption (CTRL + C)
- Shows total file size and number of lines by status code in ascending order
"""

import sys


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

    try:
        for line in sys.stdin:
            line_count += 1

            # Use simple string splitting instead of regex
            parts = line.split('"')
            if len(parts) >= 2:
                try:
                    # Get status code and file size from the part
                    info = parts[1].split()
                    if len(info) >= 2 and "GET /projects/260 HTTP/1.1" in parts[1]:
                        try:
                            # The last two elements should be status
                            http_info = parts[2].strip().split()
                            if len(http_info) >= 2:
                                status_code = http_info[0]
                                file_size = int(http_info[1])

                                # Update metrics
                                total_size += file_size
                                if status_code in status_codes:
                                    status_codes[status_code] += 1
                        except (IndexError, ValueError):
                            # Try alternative parsing if the above fails
                            try:
                                line_parts = line.split()
                                if len(line_parts) >= 9:
                                    status_code = line_parts[-2]
                                    file_size = int(line_parts[-1])

                                    # Update metrics
                                    total_size += file_size
                                    if status_code in status_codes:
                                        status_codes[status_code] += 1
                            except (IndexError, ValueError):
                                pass
                except (IndexError, ValueError):
                    pass

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_codes)
