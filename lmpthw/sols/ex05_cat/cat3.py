# import modules
# set the object from an imported class
# set the arguments
# parse the arguments
# algorithm
# print it

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('files', metavar='F', type=str, nargs='+', help='files to stream')
parser.add_argument('-n', '--numbers', action='store_true', help='add line numbers to file stream')

args = parser.parse_args()

for file in args.files:
	file_stream = open(file)

	if args.numbers:
		line_num = 1
		for line in file_stream.readlines():
			print(f"{line_num}: {line}")
			line_num += 1
	else:
		print(file_stream.read())