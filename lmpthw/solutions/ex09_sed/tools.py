import re
import sys
import pdb

# returns a tuple that contains the command and a list of before/after [for sub]
def parse_script(script):
    if script[0] == "s":
        return ('s', script.split('/')[1:3])
    elif script[0] == "r":
        return ('r', script.split(' ')[1:])
    else:
        print("Error, only s supported")
        sys.exit(1)

# prints the text stream with the modified text
def do_s(file_name, pattern, replacement):
    with open(file_name) as f:
        for line in f.readlines():
            # substitute with `replacement` based on the old text
            fixed = re.sub(pattern, replacement, line)
            # print the new text stream
            print(fixed, end="")

# for every line in FILE, print the contents of the read file along with it
def do_r(file_name, in_file_name):
    contents = open(in_file_name).read()
    with open(file_name) as f:
        for line in f.readlines():
            print(line, contents, end='')

# run either do_s or do_r based on the inputs
def apply_script(command, file_name, arguments):
    if command == "s":
        do_s(file_name, *arguments)
    elif command == "r":
        do_r(file_name, *arguments)
    else:
        print("Not supported.")
        sys.exit(1)

def sed(script, files):
    # args are actually args from the function. immutable.
    # note that when using pdb, args throws the args but it's technically undefined
    command, arguments = parse_script(script)
    for file_name in files:
        # pdb.set_trace()
        apply_script(command, file_name, arguments)

# def print_uniq_lines(file_list):
#     all_lines = set()

#     for f in file_list:
#         all_lines |= set(f.readlines())
        
#     print("".join(all_lines))

