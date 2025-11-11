def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or abs(board[i] - row) == abs(i - col):
            return False
    return True

def solve(col, board):
    if col == 8:
        print(board)
        return True
    for row in range(8):
        if is_safe(board, row, col):
            board[col] = row
            if solve(col + 1, board):
                return True
    return False

board = [-1]*8
solve(0, board)
