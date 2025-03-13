#!/usr/bin/python3
import sys
import re
import signal

# Initialize variables
total_size = 0
status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
line_count = 0

# Regular expression pattern for parsing log lines
log_pattern = r'^\S+ - \[\S+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'

def print_stats():
    """Print the accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys(), key=int):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle CTRL+C interruption"""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

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
                    print_stats()
        except Exception:
            # Skip lines that don't match the expected format
            pass
                
except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats()
    raise
