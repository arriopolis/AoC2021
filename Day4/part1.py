import sys

ns = list(map(int,next(sys.stdin).strip().split(',')))

boards = []
while sys.stdin:
    if not next(sys.stdin, False): break
    board = []
    for _ in range(5):
        board.append(list(map(int, next(sys.stdin).strip().split())))
    boards.append(board)

for n in ns:
    for board in boards:
        for i in range(5):
            for j in range(5):
                if board[i][j] == n:
                    board[i][j] = -1
        transpose_board = list(zip(*board))
        for i in range(5):
            if sum(board[i]) == -5 or sum(transpose_board[i]) == -5:
                break
        else: continue
        remaining = sum(sum(cell for cell in row if cell > 0) for row in board)
        print(remaining * n)
        break
    else: continue
    break
