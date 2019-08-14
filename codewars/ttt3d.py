def win_check(field):
    # checking x axis
    for z in range(4):
        for y in range(4):
            if field[z][y][0:4] == ['o', 'o', 'o', 'o'] or field[z][y][0:4] == ['x', 'x', 'x', 'x']:
                return True
    # checking z axis
    for x in range(4):
        for y in range(4):
            checking = []
            for z in range(4):
                checking.append(field[z][y][x])
            if checking == ['o', 'o', 'o', 'o'] or checking == ['x', 'x', 'x', 'x']:
                return True
    # checking y axis
    for z in range(4):
        for x in range(4):
            checking = []
            for y in range(4):
                checking.append(field[z][y][x])
            if checking == ['o', 'o', 'o', 'o'] or checking == ['x', 'x', 'x', 'x']:
                    return True
    # checking dioganals
    for k in range(4):
        checker1 = []
        checker2 = []
        checker3 = []
        checker4 = []
        checker5 = []
        checker6 = []
        for i in range(4):
            checker1.append(field[k][i][i])
            checker2.append(field[i][k][i])
            checker3.append(field[i][i][k])
            checker4.append(field[k][3 - i][i])
            checker5.append(field[3 - i][k][i])
            checker6.append(field[3 - i][i][k])

        for checker in [checker1, checker2, checker3, checker4, checker5, checker6,
                        [field[0][0][0], field[1][1][1], field[2][2][2], field[3][3][3]],
                        [field[0][0][3], field[1][1][2], field[2][2][1], field[3][3][0]],
                        [field[0][3][3], field[1][2][2], field[2][1][1], field[3][0][0]],
                        [field[0][3][0], field[1][2][1], field[2][1][2], field[3][0][3]]
                        ]:
            if checker == ['o', 'o', 'o', 'o'] or checker == ['x', 'x', 'x', 'x']:
                return True

    return False


def play_OX_3D(moves):
    field = [
        [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11],
            [12, 13, 14, 15]
        ],
        [
            [16, 17, 18, 19],
            [20, 21, 22, 23],
            [24, 25, 26, 27],
            [28, 29, 30, 31]
        ],
        [
            [32, 33, 34, 35],
            [36, 37, 38, 39],
            [40, 41, 42, 43],
            [44, 45, 46, 47]
        ],
        [
            [48, 49, 50, 51],
            [52, 53, 54, 55],
            [56, 57, 58, 59],
            [60, 61, 62, 63]
        ]
    ]
    # enumerate is looping over something with an 
    # automatic counter
    for idx, move in enumerate(moves):

        if idx % 2 == 0:
            field[move[2]][move[1]][move[0]] = 'o'
            if win_check(field):
                return "O wins after {} moves".format(idx+1)
        else:
            field[move[2]][move[1]][move[0]] = 'x'
            if win_check(field):
                return "X wins after {} moves".format(idx+1)

    return "No winner"