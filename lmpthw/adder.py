import argparse

# The ArgumentParser object will hold all the information necessary to parse 
# the command line into Python data types.
parser = argparse.ArgumentParser(description='Process some integers.')

# these calls tell the ArgumentParser how to take the strings on the command line 
# and turn them into objects.

# nargs 
## `+` all command-line args present are gathered into a list. 
### Additionally, an error message will be generated if there wasn’t at least
### one command-line argument present
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

# for const, you can add built in functions
parser.add_argument('--sum', dest='sum', action='store_const',
                    const=sum, default=sum,
                    help='sum the integers')

# calling parse_args() will return an object with two attributes, integers and accumulate. 
# This will inspect the command line, convert each argument to the appropriate type and 
# then invoke the appropriate action.

# args == Namespace(accumulate=<built-in function sum>, integers=[1, 2])
# Namespace == Simple class used by default by parse_args() to create 
## an object holding attributes and return it
args = parser.parse_args()

print("Sum is", args.sum(args.integers))