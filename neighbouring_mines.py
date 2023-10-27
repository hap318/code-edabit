def minesweeper_numbers(board):
    if board == []:
        return []
    rows = len(board)
    cols = len(board[0])
    values = []
    shifts = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for x in range(rows):
        for y in range(cols):
            if board[x][y] == 0:
                count = 0 
                for i in shifts:
                    x1 = x + i[0]
                    y1 = y + i[1]
                    if x1 >= 0 and y1 >= 0 and x1 < len(board) and y1 < len(board[0]):
                        if board[x+i[0]][y+i[1]] == 1:
                            count += 1
                values.append(count)

    newBoard = [[0 for x in range(rows)] for x in range(cols)]
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                newBoard[i][j] = values.pop(0)
            if board[i][j] == 1:
                newBoard[i][j] = 9
    
    return(newBoard)