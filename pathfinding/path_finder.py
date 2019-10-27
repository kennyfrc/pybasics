import pdb

def path_finder(maze):
    # build a matrix where you can draw from matrix[x][y]
    matrix = list(map(list, maze.splitlines()))
    pdb.set_trace()
    # define a stack of nodes where the neighbors aren't checked
    # len(matrix) = size of the matrix. to be used when querying matrix[x][y]
    stack, length = [[0, 0]], len(matrix)
    # while there are unexplored neighbors
    while len(stack):
      # pop the node to explore
      x, y = stack.pop()
      # if it's a dot (passable area), then mark as x
      if matrix[x][y] == '.':
        matrix[x][y] = 'x'
        # for the neighbors around the node, defined as a set of tuples
        for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
          # if it's within the bounds of the matrix, add it to the nodes to be explored
          if 0 <= x < length and 0 <= y < length:
            stack.append((x, y))
    # check if the node is == 'x'
    return matrix[length-1][length-1] == 'x'

a = "\n".join([
  ".W...",
  ".W...",
  ".W.W.",
  "...WW",
  "...W."])

print(path_finder(a))