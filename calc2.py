#!/usr/bin/env python3

# I want y to get a default value of 10.
# If I just pass x, it'll add that value to 10.

import argparse

# create a parser
parser = argparse.ArgumentParser()

# declare arguments
parser.add_argument('x', help='first numeric argument', type=int)  
parser.add_argument('y', help='second numeric argument', type=int)

# gather arguments
args = parser.parse_args()

# retrieve values
print(f'{args.x} + {args.y} = {args.x + args.y}')
