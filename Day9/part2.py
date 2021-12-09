import sys
import itertools as it

g = []
for line in sys.stdin:
    g.append(list(map(int,line.strip())))

h = len(g)
w = len(g[0])

basins = []
remaining = set(it.product(range(h), range(w)))
while remaining:
    y,x = remaining.pop()
    if g[y][x] == 9: continue
    size = 1
    frontier = set([(y,x)])
    while frontier:
        y,x = frontier.pop()
        for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
            newy,newx = y+dy,x+dx
            if newy < 0 or newy >= h: continue
            if newx < 0 or newx >= w: continue
            if (newy,newx) not in remaining: continue
            remaining.remove((newy,newx))
            if g[newy][newx] == 9: continue
            frontier.add((newy,newx))
            size += 1
    basins.append(size)

tot = 1
for a in sorted(basins, reverse = True)[:3]:
    tot *= a
print(tot)
