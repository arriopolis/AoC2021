import sys
import itertools as it

grid = []
for line in sys.stdin:
    grid.append(list(map(int, line.strip())))

h,w = len(grid),len(grid[0])
num_flashes = 0
for t in range(100):
    frontier = set()
    for y in range(h):
        for x in range(w):
            if grid[y][x] < 9: grid[y][x] += 1
            else: frontier.add((y,x))
    while frontier:
        y,x = frontier.pop()
        grid[y][x] = 0
        num_flashes += 1
        for dy,dx in it.product(range(-1,2), repeat = 2):
            if dy == dx == 0: continue
            newy,newx = y+dy,x+dx
            if newy < 0 or newy >= h: continue
            if newx < 0 or newx >= w: continue
            if grid[newy][newx] == 0: continue
            if grid[newy][newx] == 9: frontier.add((newy,newx))
            else: grid[newy][newx] += 1

print(num_flashes)
