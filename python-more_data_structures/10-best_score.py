#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    sorted_items = sorted((v, k) for k, v in a_dictionary.items())
    return sorted_items[-1][1]
