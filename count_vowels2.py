#!/usr/bin/env python3

# what I really want is for argparse to take the filename,
# open the file, and make it available for reading

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', help='name of the file', required=True, type=argparse.FileType('r'))  

# gather arguments
args = parser.parse_args()

# retrieve values
total = 0

for one_line in args.f:
    for one_character in one_line:
        if one_character in 'aeiou':
            total += 1
            
print(f'Vowel count: {total}')            