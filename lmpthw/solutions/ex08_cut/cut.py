import sys
import pdb

_, delim, fields = sys.argv
# array of integers
split_at = [int(x) for x in fields.split(',')]


while True:
    try:
        # pdb.set_trace()
        print(f"\nType some text that you want to cut, based the delimeter \"{delim}\":")
        line = input()
        # split the string by the delimeter
        cuts = line.split(delim)
        
        for i in split_at:
            # print each of the cuts
            # the end= just removes the newline default at the end
            print(f"{cuts[i]} ", end="")
        print()

    except EOFError:
        sys.exit(0)
    except IndexError:
        pass