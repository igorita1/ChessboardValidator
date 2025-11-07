
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

def main():
    # Board that passes all rules
    correctBoard = {'a1': 'wrook','b1': 'wknight','c1': 'wbishop','d1': 'wking','e1': 'wqueen','f1': 'wbishop','g1': 'wknight','h1': 'wrook','a2': 'wpawn','b2': 'wpawn','c2': 'wpawn','d2': 'wpawn','e2': 'wpawn','f2': 'wpawn','g2': 'wpawn','h2': 'wpawn','a7': 'bpawn','b7': 'bpawn','c7': 'bpawn','d7': 'bpawn','e7': 'bpawn','f7': 'bpawn','g7': 'bpawn','h7': 'bpawn','a8': 'brook','b8': 'bknight','c8': 'bbishop','d8': 'bking','e8': 'bqueen','f8': 'bbishop','g8': 'bknight','h8': 'brook'}
    # Board that fails all rules
    incorrectBoard = {'b1': 'wrook','e1': 'wbishop','z9': 'wrook','a2': 'wpawn','b2': 'wpawn','c2': 'wknight','d2': 'wqueen','e2': 'wkingz','h2': 'wpawn','b3': 'wbishop','f3': 'wpawn','g3': 'wpawn','h3': 'bknight','c4': 'wknight','d4': 'wpawn','g4': 'bqueen','d5': 'bknight','c6': 'bpawn','a7': 'bpawn','b7': 'bpawn','e7': 'bpawn','f7': 'bpawn','g7': 'bpawn','h7': 'bpawn','b8': 'brook','d8': 'bbishop','e8': 'bbishop','g8': 'bking','h8': 'brook'}
    print(validator(correctBoard)) # Should print True
    print(validator(incorrectBoard)) # Should print False

main()
