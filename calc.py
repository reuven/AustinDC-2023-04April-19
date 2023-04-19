#!/usr/bin/env python3

import argparse

# create a parser
parser = argparse.ArgumentParser()

# declare arguments
parser.add_argument('x', description='first numeric argument', type=int)  
parser.add_argument('y', description='second numeric argument', type=int)

# gather arguments
args = parser.parse_args()

# retrieve values
print(f'{args.x} + {args.y} = {args.x + args.y}')
