import pdb

# solution: append braces on the stack of keys
# remove braces if there's a match
# return if the length of the stack is 0

def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        pdb.set_trace()
        if character in braces.keys():
            stack.append(character)
        else:
        	# pop() permanently removes the key
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0  

validBraces("{[]}")