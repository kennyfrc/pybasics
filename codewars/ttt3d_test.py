import unittest
import ttt3d

Test.describe("Sample tests")

Test.it("No moves")
test.assert_equals(play_OX_3D([]), "No winner")



Test.it("Not many moves")
moves = [
    [0,0,0],
    [1,1,1],
    [2,2,2],
    [3,3,3]
]
test.assert_equals(play_OX_3D(moves), "No winner")



Test.it("oWins")
moves = [
    [0,2,1], # O
    [0,2,2],
    [1,2,1], # O  
    [1,2,2],
    [2,2,1], # O
    [2,2,2],
    [3,2,1]  # O  
]
test.assert_equals(play_OX_3D(moves), "O wins after 7 moves")



Test.it("xWins")
moves = [
    [0,1,1],
    [0,0,0], # X
    [0,2,2],
    [1,1,1], # X  
    [1,2,2],
    [2,2,2], # X
    [2,1,2],
    [3,3,3], # X  
    [0,2,1]
]
test.assert_equals(play_OX_3D(moves), "X wins after 8 moves")
