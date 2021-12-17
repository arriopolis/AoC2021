import sys
import itertools as it

x,y = sys.stdin.read().strip()[13:].split(', ')
xmin,xmax = map(int,x.split('=')[1].split('..'))
ymin,ymax = map(int,y.split('=')[1].split('..'))

ctr = 0
for vx,vy in it.product(
            range(min(xmin,0),max(0,xmax)+1),
            range(-max(abs(ymin),abs(ymax)+1),max(abs(ymin),abs(ymax)+1))
        ):
    x,y = 0,0
    while y > ymin:
        x += vx
        y += vy
        vx = vx - 1 if vx > 0 else vx + 1 if vx < 0 else 0
        vy -= 1
        if xmin <= x <= xmax and ymin <= y <= ymax: break
    else: continue
    ctr += 1
print(ctr)
