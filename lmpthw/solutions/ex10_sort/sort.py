import sys
import pdb

lines = []

if len(sys.argv) > 1:
    for file_name in sys.argv[1:]:
        lines += [line for line in open(file_name).readlines() if len(line) > 20]
else:
    while True:
        try:
            line = input() + "\n"
            # pdb.set_trace()
            lines.append(line)
            print(sorted(lines))
            
        except EOFError:
            break

print("".join(sorted(lines)), end="")
