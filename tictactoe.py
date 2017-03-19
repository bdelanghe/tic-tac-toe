# board = [{0:0,1:0,2:1},{0:1,1:1,2:3},{0:1,1:1,2:3}]

size = int(input('How large do you want the board?'))
print(size)
board = []
for x in xrange(size):
    row = {}
    k = 0
    for x in xrange(size):
        row[k] = 0
    print(row)
    board.append(row)

end = False
players = {1:'X',2:'O'}
turn = 0


def draw(brd):
    global start
    global players

    for l in brd:
        row = ''
        for i in l:
            for p in players:
                if l[i] == p:
                    row = row + players[p]
            if l[i] == 0:
                row = row + ' '
        print(row)

def checkwin(brd):
    global end
    global players

    playerwin = {}
    for p in players:
        playerwin[p] = 0

#Check if Rows allow for win
    rowwin = {}
    for p in players:
        rowwin[p] = True
        for l in brd:
            if l[0] == p:
                for i in l:
                    if l[i] != p:
                        rowwin[p] = False
            else:
                rowwin[p] = False
            playerwin[p] += rowwin[p]
    # print(rowwin)

# Check if Column allows for win
    colwin = {}
    for p in players:
        colwin[p] = True
        col = 0
        while col <= len(brd[0]) - 1:
            if brd[0][col] == p:
                for l in brd:
                    if l[col] != p:
                        colwin[p] = False
            else:
                colwin[p] = False
            playerwin[p] += colwin[p]
            col += 1
    # print(colwin)

# Check if diangnal allows for win
    diwin = {}
    for p in players:
        diwin[p] = True
        if brd[0][0] == p:
            di = 0
            for l in brd:
                if l[di] != p:
                    diwin[p] = False
                di += 1
        else:
            diwin[p] = False
        playerwin[p] += diwin[p]
    # print(diwin)

# Check if diangnal allows for win
    diwin2 = {}
    for p in players:
        diwin2[p] = True
        if brd[0][len(brd[0]) - 1] == p:
            di = 0
            for l in brd:
                if l[len(brd[0]) - 1 - di] != p:
                    diwin2[p] = False
                di += 1
        else:
            diwin2[p] = False
        playerwin[p] += diwin2[p]
    # print(diwin2)

#declare if there was a winner
    for p in players:
        if playerwin[p] > 0:
            print(players[p] + 's Won!')
            end = True



draw(board)
checkwin(board)
