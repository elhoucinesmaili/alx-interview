#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''Calculates the fewest number of operations needed 
    to get exactly n 'H' characters using Copy All and Paste.
    
    Returns:
        Integer: minimum operations, or 0 if impossible
    '''
    pasted_chars = 1  # current number of 'H's in the file
    clipboard = 0     # current number of copied 'H's
    counter = 0       # number of operations performed

    while pasted_chars < n:
        # If nothing is copied yet, do Copy All
        if clipboard == 0:
            clipboard = pasted_chars
            counter += 1

        # If only one 'H' so far, we must Paste
        if pasted_chars == 1:
            pasted_chars += clipboard
            counter += 1
            continue

        remaining = n - pasted_chars  # how many more 'H's we need

        # If clipboard has more than remaining, it's impossible
        if remaining < clipboard:
            return 0

        # If remaining can't be divided evenly, just Paste
        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:
            # Else, Copy All and then Paste
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2

    # Return operations if exactly n 'H's, else 0
    return counter if pasted_chars == n else 0
