import sys

itr = iter(sys.stdin)
alg = next(itr).strip()
next(itr)

grid = []
for line in itr:
    grid.append(list(map(lambda c : 1 if c == '#' else 0, line.strip())))

# Enlarge the grid
n = 50
grid = [[0]*(2*n + len(grid)) for _ in range(n)] + [[0]*n + r + [0]*n for r in grid] + [[0]*(2*n + len(grid)) for _ in range(n)]

outside = 0
for _ in range(n):
    new_grid = [[0]*len(grid[0]) for _ in grid]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            s = ''
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if y+dy < 0 or y+dy >= len(grid): s += str(outside)
                    elif x+dx < 0 or x+dx >= len(grid): s += str(outside)
                    else: s += str(grid[y+dy][x+dx])
            new_grid[y][x] = 1 if alg[int(s,2)] == '#' else 0
    if alg[0] == '#': outside = 1 - outside
    grid = new_grid
print(sum(sum(r) for r in grid))
