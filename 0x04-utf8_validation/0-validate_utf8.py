#!/usr/bin/python3
"""UTF-8 Validator."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid
    UTF-8 encoding.

    Args:
        data (int[]): A list of integers where each integer represents
        a byte of data.

    Returns:
        bool: True if the data represents a valid UTF-8 encoding;
        otherwise False.
    """
    num_bytes = 0
    continuation_mask = 0b10000000
    continuation_value = 0b10000000

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            if (byte >> 7) == 0:
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (byte & continuation_mask) != continuation_value:
                return False
            num_bytes -= 1

    return num_bytes == 0
