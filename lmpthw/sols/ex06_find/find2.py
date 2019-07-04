# parse args
# find name
# not a good one

from pathlib import Path
import sys
import argparse
import pdb

def find_name(paths, name):
	ps = Path(paths[0])
	for path in ps.rglob(name):
		print(path)

def find_type(paths, type, name):
	if type not in ['d', 'f']:
		print("not a file or directory")
		sys.exit(1)
	else:
		ps = Path(paths[0])
		for path in ps.rglob(name):
			print(path)


def parse_args():
	parser = argparse.ArgumentParser()

	parser.add_argument('paths', type=str, nargs=1)
	parser.add_argument('--name', type=str)
	parser.add_argument('--type', type=str)

	return parser.parse_args()


args = parse_args()
print(args)

find_type(args.paths, args.type, args.name)