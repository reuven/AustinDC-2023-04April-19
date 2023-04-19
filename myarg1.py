#!/usr/bin/env python3

import sys

print(f'{sys.argv=}')   # print all of sys.argv

# iterate over sys.argv, printing its elements
# along with their indexes
for index, one_arg in enumerate(sys.argv):
    print(f'{index}: {one_arg}')
