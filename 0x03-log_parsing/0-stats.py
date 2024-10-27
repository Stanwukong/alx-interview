#!/usr/bin/python3
"""Computes metrics from input."""
import re
import signal
import sys


total_file_size = 0
line_count = 0
status_code_counts = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
        r' - \['
        r'(?P<date>[^\]]+)\]'
        r' "GET /projects/260 HTTP/1\.1"'
        r' (?P<status>\d+)'
        r' (?P<size>\d+)'
        )

def print_stats():
    """
    Prints the statistics: total file size and the count of
    each status code.
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")

def process_line(line):
    """
    Processes a single log line to extract metrics if the line
    matches the expected format. Uses regular expression matching
    to ensure format adherence.
    """
    global total_file_size, line_count

    match = log_pattern.match(line)
    if match:
        status = match.group("status")
        size = match.group("size")

        total_file_size += int(size)
        line_count += 1

        if status in status_code_counts:
            status_code_counts[status] += 1

def handle_interrupt(signal, frame):
    """
    Signal handler to print stats on keyboard interrupt (CTRL + C).
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_interrupt)


try:
    for line in sys.stdin:
        process_line(line.strip())

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
