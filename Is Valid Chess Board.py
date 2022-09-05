# checks if the chess board is valid
# -1 black/white king
# -each player has 16 pieces at most
# -each player has at most 8 pawns
# -all pieces must be between "1a" to "8h"
# -piece names between with "w" or "b", followed by "pawn", "knight", "bishop", "rock", "queen", or "king"

def is_valid_chess_board(test_chess):
    count = {}
    valid_number = ["1", "2", "3", "4", "5", "6", "7", "8"]
    valid_letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
    color = ["b", "w"]
    piece = ["pawn", "knight", "bishop", "rock", "queen", "king"]
    num_of_black = 0
    num_of_white = 0

# Counts amount of each piece
    for i in test_chess.values():
        count.setdefault(i, 0)
        count[i] += 1

# Checks to see if there is more than one black/ white king
    for j in ["bking", "wking"]:
        if count[j] > 1:
            return False

# Counts the number of pieces each player/color has
    for k in test_chess:
        if k[0] == color[0]:
            num_of_black += 1
            print(num_of_black)
        elif k[0] == color[1]:
            num_of_white += 1
            print(num_of_white)

# Checks if there is 16 pieces for each player at most
    if (num_of_black or num_of_white) > 16:
        return False

# Checks if each player has 8 pawns at most
    for x in ["bpawn", "wpawn"]:
        if x in count.keys():
            if count[x] not in range(1, 9):
                return False

# Checks if pieces are between "1a" to "8h"
    for y in test_chess.keys():
        if y[0] not in valid_number:
            return False
        if y[1] not in valid_letter:
            return False

# Checks if pieces contain "w" or "b", followed by "pawn", "knight", "bishop", "rock", "queen", or "king:
    for z in test_chess.values():
        if z[0] not in color:
            return False
        if z[1:] not in piece:
            return False
    return True


print(is_valid_chess_board({"6c": "bking", "8g": "wking", "1a": "wqueen", "1b": "bbishop", "1c": "bqueen",
                            "1d": "bpawn", "1e": "brock", "1f": "bknight", "2a": "bpawn", "2b": "bpawn", "2c": "bpawn",
                            "2d": "bpawn", "2e": "bpawn", "2f": "bpawn", "3a": "bpawn", "3b": "bbishop",
                            "3c": "brock", "3d": "bknight", "3e": "bknight"}))
