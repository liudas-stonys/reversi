import random


def resetBoard(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def getNewBoard():
    board = []
    for i in range(8):
        board.append([' '] * 8)
    return board


def getBoardCopy(board):
    dupeBoard = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard


def drawBoard(board):
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |       |       |       |       |       |       |       |       |'
    print('    1   2   3   4   5   6   7   8')
    print(HLINE)

    for y in range(8):
        # print(VLINE)
        print(y + 1, end=' ')
        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')
        print('|')
        # print(VLINE)
        print(HLINE)


def getValidMoves(board, tile):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return validMoves


def getBoardWithValidMoves(board, tile):
    dupeBoard = getBoardCopy(board)
    for x, y in getValidMoves(dupeBoard, tile):
        dupeBoard[x][y] = '?'
    return dupeBoard


def isOnBoard(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <= 7


def isOnCorner(x, y):
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)


def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'
    tilesToFlip = []

    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        if isOnBoard(x, y) and board[x][y] == tile:
            continue

        while isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection

        if isOnBoard(x, y) and board[x][y] == tile:
            while not (x == xstart and y == ystart):
                x -= xdirection
                y -= ydirection
                tilesToFlip.append([x, y])

    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip


def enterPlayerTile():
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Pasirinkite už ką žaisite: X ar O?')
        tile = input().upper()
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if 1 == 0:
        return 'Kompiuteris eina'
    else:
        return 'Jūs einate'


def getPlayerMove(board, playerTile):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        move = input('Įveskite savo ėjimą: ').lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                print('Toks ėjimas negalimas!\nĮveskite "hints", jei norite pagalbos.\nArba "quit", jei norite išeiti.')
                continue
            else:
                break
        else:
            print(
                'Tokio ėjimo nėra!\n\nPirma įveskite X koordinatę nuo 1 iki 8, paskui be jokio tarpo Y\nkoordinatę, taip pat nuo 1 iki 8.\n\nPavyzdžiui, 81 yra viršutinio dešiniojo kampo koordinatė.')
    return [x, y]


def getComputerMove(board, computerTile):
    global bestMove
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
    bestScore = -1

    for x, y in possibleMoves:
        dupeBoard = getBoardCopy(board)
        makeMove(dupeBoard, computerTile, x, y)
        score = getScoreOfBoard(dupeBoard)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove


def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True


def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O': oscore}


def showPoints(mainBoard, playerTile, computerTile):
    scores = getScoreOfBoard(mainBoard)
    print('\nJūs turite %s taškų(-us). Kompiuteris turi %s taškų(-us).\n' % (scores[playerTile], scores[computerTile]))


def playAgain():
    print('\nŽaisti dar kartą? (įveskite "taip" arba "ne")')
    return input().lower().startswith('t')
