def tic_tac_toe(board):
    if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
        return board[1][1]
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        elif len(set(board[i])) == 1:
            return board[i][0]
    return "Draw"


print(tic_tac_toe([
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]))

print(tic_tac_toe([
    ["O", "O", "O"],
    ["O", "X", "X"],
    ["E", "X", "X"]
]))

print(tic_tac_toe([
    ["X", "X", "O"],
    ["O", "O", "X"],
    ["X", "X", "O"]
]))

print(tic_tac_toe([
    ["X", "O", "E"],
    ["X", "O", "E"],
    ["E", "O", "X"]
]))
