#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('t', help='tuple of stuff', type=tuple)

# gather arguments
args = parser.parse_args()

# retrieve values
print(args)
