import argparse

parser = argparse.ArgumentParser(description="Just shows a sample list of help messages")

parser.add_argument('-i', '-I', action='store_false',help="creates an insight")
parser.add_argument('-f', '-F', action='store_false',help="takes flight")
parser.add_argument('numbers', metavar="numbers", type=str, nargs='+',help="shows random numbers")

args = parser.parse_args()
print(args)
print(args.numbers)

# 1. Getting help with – help or -h. 
# 2. At least three arguments that are flags, meaning they don’t take an extra argument but simply putting them on the command line turns something on. 
# 3. At least three arguments that are options, meaning they do take an argument and set a variable in your script to that option. 
# 4. Additional “positional” arguments, which are lists of files at the end of all the – style arguments and can handle Terminal wildcards like */.txt.
