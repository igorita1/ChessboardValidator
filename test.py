from chessboardValidator import validator
# Board that passes all rules
correctBoard = {'a1': 'wrook','b1': 'wknight','c1': 'wbishop','d1': 'wking','e1': 'wqueen','f1': 'wbishop','g1': 'wknight','h1': 'wrook','a2': 'wpawn','b2': 'wpawn','c2': 'wpawn','d2': 'wpawn','e2': 'wpawn','f2': 'wpawn','g2': 'wpawn','h2': 'wpawn','a7': 'bpawn','b7': 'bpawn','c7': 'bpawn','d7': 'bpawn','e7': 'bpawn','f7': 'bpawn','g7': 'bpawn','h7': 'bpawn','a8': 'brook','b8': 'bknight','c8': 'bbishop','d8': 'bking','e8': 'bqueen','f8': 'bbishop','g8': 'bknight','h8': 'brook'}
# Board that fails all rules
incorrectBoard = {'b1': 'wrook','e1': 'wbishop','z9': 'wrook','a2': 'wpawn','b2': 'wpawn','c2': 'wknight','d2': 'wqueen','e2': 'wkingz','h2': 'wpawn','b3': 'wbishop','f3': 'wpawn','g3': 'wpawn','h3': 'bknight','c4': 'wknight','d4': 'wpawn','g4': 'bqueen','d5': 'bknight','c6': 'bpawn','a7': 'bpawn','b7': 'bpawn','e7': 'bpawn','f7': 'bpawn','g7': 'bpawn','h7': 'bpawn','b8': 'brook','d8': 'bbishop','e8': 'bbishop','g8': 'bking','h8': 'brook'}
print(validator(correctBoard)) # Should print True
print(validator(incorrectBoard)) # Should print False
