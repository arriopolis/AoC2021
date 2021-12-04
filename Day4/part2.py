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
    todel = []
    for k,board in enumerate(boards):
        for i in range(5):
            for j in range(5):
                if board[i][j] == n:
                    board[i][j] = -1
        transpose_board = list(zip(*board))
        for i in range(5):
            if sum(board[i]) == -5 or sum(transpose_board[i]) == -5:
                todel.append(k)
                break
    for k in sorted(todel, reverse = True):
        if len(boards) == 1:
            remaining = sum(sum(cell for cell in row if cell > 0) for row in boards[0])
            print(remaining * n)
        del boards[k]
