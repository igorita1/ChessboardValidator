
# Takes in the Chess Board as a python dictionary, returns True if correct and False if incorrect.
# Checks for:
#   (1) Both Kings Exist on the board.
#   (2) Each player has at most 16 pieces.
#   (3) Each player has at most 8 pawns.
#   (4) Every piece must be on valid space on the board (1a to 8h).
#   (5) Piece names begin with 'w' or 'b' and piece names must be either 'pawn', 'rook', 'bishop', 'knight', 'queen', and 'king'.

def validator(board):
    whitePieces, whitePawns, whiteKing = 0, 0, 0
    blackPieces, blackPawns, blackKing = 0, 0, 0
    totalPieces, validSpaces, validPieces = 0, 0, 0
    validNames = ['pawn', 'knight', 'bishop', 'rook', 'king', 'queen']
    validLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    validNumbers = ['1', '2', '3', '4', '5', '6', '7', '8']


    for coordinate, piece in board.items():
        totalPieces += 1
        color = piece[0]
        name = piece[1:]
        # Checking for rules (1), (2), (3), and (5)
        if color == 'w':
            if name in validNames:
                whitePieces += 1
                validPieces += 1
                if name == 'pawn':
                    whitePawns += 1
                elif name == 'king':
                    whiteKing += 1
        elif color == 'b':
            if name in validNames:
                blackPieces += 1
                validPieces += 1
                if name == 'pawn':
                    blackPawns += 1
                elif name == 'king':
                    blackKing += 1
        # Checking for rule (4)
        if coordinate[0] in validLetters and coordinate[1:] in validNumbers:
            validSpaces += 1

    # Final check to see if all rules stay true
    if (whiteKing == 1) and (blackKing == 1) and (whitePieces <= 16) and (blackPieces <= 16) and (whitePawns <= 8) and (blackPawns <= 8) and (validSpaces == totalPieces) and (validPieces == totalPieces):
        return True
    else:
        return False



