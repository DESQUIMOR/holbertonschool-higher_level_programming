#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key with the highest integer value in a dictionary."""
    if a_dictionary:
        a = sorted((value, key) for key, value in a_dictionary.items()).pop()[1]
        return a
