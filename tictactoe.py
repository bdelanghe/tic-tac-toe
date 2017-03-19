board = [{0:0,1:2,2:2},{0:1,1:2,2:2},{0:2,1:1,2:2}]
start = True
end = False
players = {1:'X',2:'O'}


def draw(brd):
    global start
    global players
    if start == True:
        print('lets begin')
    start = False

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
    for l in brd:
        win = {}
        for p in players:
            win[p] = True
        print(win)
        rowwinx = True
        rowwino = True

#check for row win x
        if l[0] == 1:
            for i in l:
                if l[i] == 2 or l[i] == 0:
                    rowwinx = False
            # if rowwinx == True:
            #     print("row win X")
            playerwin[1] += rowwinx
#check for row win o
        if l[0] == 2:
            for i in l:
                if l[i] == 1 or l[i] == 0:
                    rowwino = False
            # if rowwino == True:
            #     print("row win O")
            playerwin[2] += rowwinx

#Check if Column allows for win
#check if x is possible
    col = 0
    length = len(brd[0]) - 1

    while col <= length:
        colwinx = True
        if brd[0][col] == 1:
            for l in brd:
                if l[col] == 2 or l[col] == 0:
                    colwinx = False
            # if colwinx == True:
            #     print("Col win X")
            playerwin[1] += colwinx
        col += 1

    col = 0
#check if o is possible
    while col <= length:
        colwino = True
        if brd[0][col] == 2:
            for l in brd:
                if l[col] == 1 or l[col] == 0:
                    colwino = False
            # if colwino == True:
            #     print("Col win O")
            playerwin[2] += colwino
        col += 1

# check diagnal win
  # x first
    diwinx = True
    if brd[0][0] == 1:
        di = 0
        for l in brd:
            if l[di] == 2 or l[di] == 0:
                diwinx = False
            di += 1
        # if diwinx == True:
        #     print("Downward Di win X")
        playerwin[1] += diwinx

#   o next
    diwino = True
    if brd[0][0] == 2:
        di = 0
        for l in brd:
            if l[di] == 1 or l[di] == 0:
                diwino = False
            di += 1
        # if diwino == True:
        #     print("Downward Di win O")
        playerwin[2] += diwino

#upwards diagnal win
    diwinx = True
    if brd[0][length] == 1:
        di = 0
        for l in brd:
            if l[length - di] == 2 or l[length - di] == 0:
                diwinx = False
            di += 1
        # if diwinx == True:
        #     print("Upward Di win X")
        playerwin[1] += diwinx

    diwino = True
    if brd[0][length] == 2:
        di = 0
        for l in brd:
            if l[length - di] == 1 or l[length - di] == 0:
                diwino = False
            di += 1
        # if diwino == True:
        #     print("Upward Di win O")
        playerwin[2] += diwino




#declare if there was a winner
    for p in players:
        if playerwin[p] > 0:
            print(players[p] + 's Won!')
            end = True



draw(board)
checkwin(board)
