#!/usr/bin/env python3

# this program will take a filename as an argument,
# and will print the number of vowels (a, e, i, o, u)
# it finds in that file.  (We assume it's a text file.)

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', help='name of the file', required=True)  

# gather arguments
args = parser.parse_args()

# retrieve values
total = 0

for one_line in open(args.f):
    for one_character in one_line:
        if one_character in 'aeiou':
            total += 1
            
print(f'Vowel count: {total}')            