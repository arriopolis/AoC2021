import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))
h,w = len(grid),len(grid[0])

changed = True
ctr = 0
while changed:
    changed = False
    ctr += 1
    to_move = set()
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '>' and grid[i][(j+1)%w] == '.':
                to_move.add(((i,j),(i,(j+1)%w)))
                changed = True
    for (i,j),(i2,j2) in to_move:
        grid[i2][j2] = grid[i][j]
        grid[i][j] = '.'

    to_move = set()
    for j in range(w):
        for i in range(h):
            if grid[i][j] == 'v' and grid[(i+1)%h][j] == '.':
                to_move.add(((i,j),((i+1)%h,j)))
                changed = True
    for (i,j),(i2,j2) in to_move:
        grid[i2][j2] = grid[i][j]
        grid[i][j] = '.'

print(ctr)
