#!/usr/bin/env python3

import argparse

# create a parser
parser = argparse.ArgumentParser()

# declare arguments
parser.add_argument('x')   # any argument I define with add_argument...
parser.add_argument('y')

# gather arguments
args = parser.parse_args()

# retrieve values
print(args)
print(args.x)              # ... can be retrieved as an attribute from our parsed args
print(args.y)

