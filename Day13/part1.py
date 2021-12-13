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

c,n = folds[0]
if c == 'y':
    dots = set([(x, min(y, 2*n - y)) for x,y in dots])
else:
    dots = set([(min(x, 2*n - x), y) for x,y in dots])
print(len(dots))
