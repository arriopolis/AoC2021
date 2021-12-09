import sys

g = []
for line in sys.stdin:
    g.append(list(map(int,line.strip())))

h = len(g)
w = len(g[0])

tot = 0
for y in range(h):
    for x in range(w):
        n = g[y][x]
        m = n
        for dy in range(-1,2):
            for dx in range(-1,2):
                if dy == dx == 0: continue
                newy,newx = y+dy,x+dx
                if newy < 0 or newy >= h: continue
                if newx < 0 or newx >= w: continue
                m = min(m, g[newy][newx])
        if m == n:
            tot += n + 1
print(tot)
