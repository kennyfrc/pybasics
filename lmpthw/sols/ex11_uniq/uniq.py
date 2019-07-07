#!/usr/bin/env python3.6

import sys

def print_uniq_lines(file_list):
	# initialize a set
    all_lines = set()

    for f in file_list:
    	# if empty, then check f.readlines()
    	# then set it to all_ines
        all_lines |= set(f.readlines())
    # turn the set into a string by joining it to ""    
    print("".join(all_lines))

if len(sys.argv) > 1:
	# open a TextIOWrapper file for each file in sys.argv
    print_uniq_lines(open(f) for f in sys.argv[1:])
else:
    print_uniq_lines([sys.stdin])

