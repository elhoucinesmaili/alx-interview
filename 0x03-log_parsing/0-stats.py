#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys

# Dictionary to count occurrences of specific HTTP status codes
cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}

# Variable to keep track of total file size
total_size = 0

# Counter to count lines read (used to print metrics every 10 lines)
counter = 0

try:
    # Read lines from standard input
    for line in sys.stdin:
        # Split line into components based on spaces
        line_list = line.split(" ")
        if len(line_list) > 4:
            # Extract status code and file size from the line
            code = line_list[-2]
            size = int(line_list[-1])
            # If the status code is one we're tracking, increment its count
            if code in cache.keys():
                cache[code] += 1
            # Add to the total file size
            total_size += size
            # Increment line counter
            counter += 1

        # Every 10 lines, print metrics
        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

# Ignore any exceptions that occur
except Exception as err:
    pass

finally:
    # Always print final metrics when the script ends
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
