#!/usr/bin/python3
print("".join(
    "{}".format(chr(c - (32 if c % 2 == 1 else 0)))
    for c in range(122, 96, -1)
), end="")
