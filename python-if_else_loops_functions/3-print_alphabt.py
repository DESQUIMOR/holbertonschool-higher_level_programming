#!/usr/bin/python3
for letter in range(97, 123):
        if letter != 101 or chr(letter) != 113:
                print("{}".format(chr(letter)), end="")
