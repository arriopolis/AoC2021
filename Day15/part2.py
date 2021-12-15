import sys,heapq

grid = []
for line in sys.stdin:
    l = list(map(int,line.strip()))
    grid.append(sum(([((c+i-1)%9+1) for c in l] for i in range(5)), []))

origh = len(grid)
for i in range(4):
    for l in grid[:origh]:
        grid.append([(c+i)%9+1 for c in l])

h = len(grid)
w = len(grid[0])

r = [[float('inf')]*w for _ in range(h)]
r[0][0] = 0
q = [(0,(0,0))]
while q:
    s,(x,y) = heapq.heappop(q)
    if r[y][x] != s: continue
    for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
        newx,newy = x+dx,y+dy
        if newx < 0 or newx >= w: continue
        if newy < 0 or newy >= h: continue
        news = s + grid[newy][newx]
        if news >= r[newy][newx]: continue
        r[newy][newx] = news
        heapq.heappush(q, (news, (newx,newy)))
print(r[-1][-1])
