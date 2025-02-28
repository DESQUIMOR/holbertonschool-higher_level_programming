#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorted_items = sorted((value, key) for key, value in a_dictionary.items())
        return sorted_items.pop()[1]
