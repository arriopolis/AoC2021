import sys

dots = set()
itr = iter(sys.stdin)
for line in itr:
    if not line.strip(): break
    x,y = map(int,line.strip().split(','))
    dots.add((x,y))

folds = []
for line in itr:
    c,n = line.strip()[11:].split('=')
    folds.append((c,int(n)))

for c,n in folds:
    if c == 'y':
        dots = set([(x, min(y, 2*n - y)) for x,y in dots])
    else:
        dots = set([(min(x, 2*n - x), y) for x,y in dots])

xmax,ymax = max(x for x,y in dots),max(y for x,y in dots)
ss = []
for y in range(ymax+1):
    s = []
    for x in range(xmax+1):
        s.append('#' if (x,y) in dots else '.')
    ss.append(''.join(s))
print('\n'.join(ss))
