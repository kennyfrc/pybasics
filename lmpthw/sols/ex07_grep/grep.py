import re
import sys
import argparse
from pathlib import Path
import pdb

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('pattern', type=str, nargs=1) 
    parser.add_argument('start', type=str, nargs=1) 
    parser.add_argument('-r', action='store_true')

    return parser.parse_args()

def find_in_file(name, pattern):
    try:
        # open(name) returns a TextIOWrapper
        # open(name).readlines() returns a string containing the text
        lines = open(name).readlines()
    #  an illegal sequence of str characters will cause the coding-specific decode() to fail
    except UnicodeDecodeError:
        print(f"Binary file {name} matches.")
        return

    # Compile a regular expression pattern into a regular expression object,
    ## which can be used for matching using its match(), search() and other methods
    ### expr is a RE object where u can do search() and match()
    expr = re.compile(pattern)

    for line in lines:
        # expr.search() -> Match objects always have a boolean value of True
        # expr.match() => If zero or more characters at the beginning of string match this 
        ## regular expression, return a corresponding match object. 
        if expr.search(line):
            print(line, end="")

args = parse_args()
print(args)

# args.r = recrusively search subdirectories
## since the "*" will do that
if args.r:
    start_path = Path(args.start[0])
    # rglob searches for multiple directories no matter the level
    for f in start_path.rglob("*"):
        # if the item that matches the rglob list, then validate if it's a file
        # if ti's a file, then rujn find_in_file which prints lines
        if f.is_file():
            find_in_file(f, args.pattern[0])
else:
    # standard search
    find_in_file(args.start[0], args.pattern[0])
