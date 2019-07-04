# for each file in the file LIST
## open the file
## if args numbers exist
### print each line with the number
## else  
### print the file by just reading it


import argparse
import pdb
parser = argparse.ArgumentParser()

parser.add_argument('files', metavar='F', help="file", type=str, nargs='+')
parser.add_argument('-n', '--numbers', action='store_true',
        help='Print line numbers')

args = parser.parse_args()

print(">>> parsed args: ", args)

line_number = 1
for in_file_name in args.files:
    pdb.set_trace()
	# in_file is a TextIOWrapper which inherits from TextIOBaseClass
	# Base class for text streams. This class provides a unicode character 
	# and line based interface to stream I/O
    in_file = open(in_file_name)
    if args.numbers:
        for line in in_file.readlines():
        	# print(f"{}")A formatted string literal or f-string is a string literal 
        	# that is prefixed with 'f' or 'F'. These strings may contain 
        	# replacement fields, which are expressions delimited by curly braces {}.
            print(f"\t{line_number}\t{line}", end="")
            line_number += 1
    else:
    	print(in_file.read())

