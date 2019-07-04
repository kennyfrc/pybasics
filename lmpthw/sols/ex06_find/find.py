# set parser, add arguments, parse arguemnts, invoke and print
# find_name, which iterates over a sorted list of name (via rglob) then prints it
# find_type, which throws an error (break) if not dir or name, but prints everything else

from pathlib import Path
import sys
import argparse
import pdb

def name_find(start, args):
    # rglob searches for multiple directories no matter the level
    # sorted(start.rglob(args.name) returns a list of PosixPaths)
    for f in start.rglob(args.name):
        # prints each one
        print(f)

def type_find(start, args):
    if args.type not in ['d','f']:
        print(f"Unknown type: {args.type}")
        sys.exit(1)

    # for every element in the a list of args.name or a wildcard
    for f in start.rglob(args.name or "*"):
        # if it's validated to be a director
        if args.type == "d" and f.is_dir(): # Path.is_dir()
            print(f)
        elif args.type == "f" and f.is_file(): # Path.is_file()
            print(f)


def find_files(args):
    # PosixPath
    start_path = Path(args.start[0])
    # check if name exists but not type
    if args.name and not args.type:
        # find a name within start_path
        name_find(start_path, args)
    # check if type exists
    elif args.type:
        # the find type within start_path
        type_find(start_path, args)
    # else, prompt to define the path
    else:
        print("You need either --name or --type")
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('start', type=str, nargs=1) 
    parser.add_argument('--name', type=str)
    parser.add_argument('--type' , type=str)

    return parser.parse_args()

print(parse_args())
find_files(parse_args())

