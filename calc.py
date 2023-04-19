#!/usr/bin/env python3

import argparse

# create a parser
parser = argparse.ArgumentParser()

# declare arguments
parser.add_argument('x')  
parser.add_argument('y')

# gather arguments
args = parser.parse_args()

# retrieve values
print(f'{args.x} + {args.y} = {args.x + args.y}')
