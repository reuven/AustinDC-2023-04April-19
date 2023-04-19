#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

class LoudTuple:
    def __init__(self, x):
        print(f'I got {x}!')
        self.x = tuple(x)

parser.add_argument('t', help='tuple of stuff', type=tuple)
parser.add_argument('n', help='more than one!', type=int, nargs='+')

# gather arguments
args = parser.parse_args()

# retrieve values
print(args)
