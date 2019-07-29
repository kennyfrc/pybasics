import sys
import tools
import pdb

# string
script = sys.argv[1]
# list. the [2:] forces it to become a list
files = sys.argv[2:]

tools.sed(script, files)
