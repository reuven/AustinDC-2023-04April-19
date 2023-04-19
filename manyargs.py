#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('n', help='number of lines to read', required=True)
parser.add_argument('-f', help='name of the file', required=True)  

# gather arguments
args = parser.parse_args()

# retrieve values
total = 0

for index, one_line in enumerate(open(args.f)):
    if index >= args.n:
        break
        
    for one_character in one_line:
        if one_character in 'aeiou':
            total += 1
            
print(f'Vowel count: {total}')            