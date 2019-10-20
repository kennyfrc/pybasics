import pdb

def simple_path_finder(maze):
    # change the string into a matrix (array of arrays)
    matrix = list(map(list, maze.splitlines()))
    # pdb.set_trace()
    # define the size
    size = len(matrix)-1
    # define the stack paths to add
    stack, stack_to_add, count = [(0,0)], [], 0
    # while there's a stack path
    while stack:
        # count it as it's a future move
        count += 1
        # while stack paths exist
        while stack:
            # remove it
            a, b = stack.pop()
            # mark your spot with an X
            matrix[a][b] = "X"
            # for each i, j among the neighboring paths
            for i, j in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
                # if it's below the size of the matrix and it's a dot
                if 0 <= i <= size and 0 <= j <= size and matrix[i][j] == '.':
                    # if it reaches the goal
                    if i == size and j == size:
                        # return the distance
                        return count
                    # else: append the 
                    stack_to_add.append((i,j))
        # once the stack (second layer) is empty...
        # convert tuple to a set
        stack, stack_to_add = list(set(stack_to_add)), []
    return False

a = "\n".join([
  ".W...",
  ".W...",
  ".W.W.",
  "...WW",
  "...W."])

b = "\n".join([
  ".WWWW",
  ".W...",
  ".W.W.",
  ".W.W.",
  "...W."])

print(simple_path_finder(a[:]))
print(simple_path_finder(b[:]))