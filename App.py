from services.GameService import *

print('\nJūs žaidžiate R E V E R S I\n')
while True:
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    showHints = False
    turn = whoGoesFirst()
    print('\n' + turn + ' pirmas.\n')

    while True:
        if turn == 'Žaidėjas':
            if showHints:
                validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)
                drawBoard(validMovesBoard)
            else:
                drawBoard(mainBoard)
            showPoints(mainBoard, playerTile, computerTile)
            move = getPlayerMove(mainBoard, playerTile)

            if move == 'quit':
                print('Ačiū, kad žaidėte!')
                exit()
            elif move == 'hints':
                showHints = not showHints
                continue

            else:
                makeMove(mainBoard, playerTile, move[0], move[1])
            if getValidMoves(mainBoard, computerTile) == []:
                break
            else:
                turn = 'Kompiuteris'

        else:
            drawBoard(mainBoard)
            showPoints(mainBoard, playerTile, computerTile)
            input('Paspaukite Enter, kad pamatytumėte kompiuterio ėjimą.\n')
            x, y = getComputerMove(mainBoard, computerTile)
            makeMove(mainBoard, computerTile, x, y)

            if getValidMoves(mainBoard, playerTile) == []:
                break
            else:
                turn = 'Žaidėjas'

    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print('\nX surinko %s taškų(-us). O surinko %s taškų(-us).' % (scores['X'], scores['O']))

    if scores[playerTile] > scores[computerTile]:
        print('\nSveikiname! Jūs nugalėjote kompiuterį %s taškais!' % (scores[playerTile]))
    elif scores[playerTile] = scores[computerTile]:
        print('\nNenusiminkite, žaidimas baigėsi lygiosiomis.')
    else:
        print('\nJūs pralaimėjote.')

    if not playAgain():
        break
exit()
