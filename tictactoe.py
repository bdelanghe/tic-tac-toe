board = [{0:0,1:0,2:0},{0:0,1:0,2:0},{0:0,1:0,2:0}]
start = True
end = False



def draw(brd):
    global start
    if start == True:
        print('lets begin')
    start = False

    for l in brd:
        row = ''
        for i in l:
            if l[i] == 1:
                row = row + ('x').ljust(1)
            if l[i] == 2:
                row = row + ('o').ljust(1)
            else:
                row = row.ljust(2)
        print(row)

def checkwin(brd):
    global end
    winx = False
    wino = False

    for l in brd:
        rowwinx = True
        rowwino = True

        if l[0] == 1:
            for i in l:
                if l[i] == 2 or l[i] == 0:
                    rowwinx = False
        if l[0] == 2:
            for i in l:
                if l[i] == 1 or l[i] == 0:
                    print(l[i])
                    rowwino = False
        if l[0] == 0:
            rowwinx = False
            rowwino = False
        winx += rowwinx
        wino += rowwinx

    col = 0
    colm = len(l)

    colwinx = True
    while col < colm:
        print(col)
        if board[0][col] == 1:
            for l in brd:
                if l[col] == 2 or l[col] == 0:
                    colwin = False
        if board[0][col] == 0:
            colwin = False
            print('false')
        col += 1
        winx += colwinx
    col = 0



    colwino = True
    while col < colm:
        print(col)
        if board[0][col] == 2:
            for l in brd:
                if l[col] == 1 or l[col] == 0:
                    colwin = False
        if board[0][col] == 0:
            colwin = False
            print('false')
        col += 1
    col = 0
    wino += colwinx

    if winx > 0:
        print('x WON!!!')
        end = True
    if wino > 0:
        print('y WON!!!')
        end = True



draw(board)
checkwin(board)
