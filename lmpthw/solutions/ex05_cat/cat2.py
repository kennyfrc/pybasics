import argparse

parser = argparse.ArgumentParser()

parser.add_argument('files', metavar='F', type=str, nargs='+')
parser.add_argument('-n', '--numbers', action='store_true', help='print line numbers' )

args = parser.parse_args()

line_num = 1
for file in args.files:
	file_stream = open(file)

	if args.numbers:
		for file_line in file_stream.readlines():
			print(f"{line_num}: {file_line}")
			line_num += 1
	else:
		print(file_stream.read())