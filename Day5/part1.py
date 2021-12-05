import sys

lines = []
for line in sys.stdin:
    start,end = line.strip().split(' -> ')
    x1,y1 = map(int, start.split(','))
    x2,y2 = map(int, end.split(','))
    lines.append((x1,y1,x2,y2))

xmin = min(min(l[0],l[2]) for l in lines)
xmax = max(max(l[0],l[2]) for l in lines)
ymin = min(min(l[1],l[3]) for l in lines)
ymax = max(max(l[1],l[3]) for l in lines)

grid = [[0 for _ in range(xmax+1)] for _ in range(ymax+1)]
for x1,y1,x2,y2 in lines:
    if not (x1 == x2) and not (y1 == y2): continue
    if abs(x1-x2) > abs(y1-y2):
        (x1,y1),(x2,y2) = min((x1,y1),(x2,y2)),max((x1,y1),(x2,y2))
        for x in range(x1,x2+1):
            y = y1 + (x-x1) * (y2-y1) // (x2-x1)
            grid[y][x] += 1
    else:
        (y1,x1),(y2,x2) = min((y1,x1),(y2,x2)),max((y1,x1),(y2,x2))
        for y in range(y1,y2+1):
            x = x1 + (y-y1) * (x2-x1) // (y2-y1)
            grid[y][x] += 1

print(sum(sum(c >= 2 for c in r) for r in grid))
