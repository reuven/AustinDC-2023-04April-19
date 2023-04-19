#!/usr/bin/env python3

# what if I want to pass the arguments in any order?
# To do that, I'll need to change them to be *keyword* arguments
# In other words, I'll have to say -x 5 and -y 3
# but I'll also be able to say -y 3 and -x 5, in that order

import argparse

# create a parser
parser = argparse.ArgumentParser()

# declare arguments
# having a - before the name of the argument makes it a keyword argument
parser.add_argument('-x', help='first numeric argument', type=int)  
parser.add_argument('-y', help='second numeric argument', type=int, default=10)

# gather arguments
args = parser.parse_args()

# retrieve values
print(f'{args.x} + {args.y} = {args.x + args.y}')
