#!/usr/bin/python3
def remove_char_at(str, n):
    """Creates a copy of the string, removing the character at index n."""
    return str[:n] + str[n+1:] if 0 <= n < len(str) else str
