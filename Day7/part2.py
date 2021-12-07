import sys
xs = sorted(map(int,sys.stdin.read().strip().split(',')))

xmin,xmax = min(xs),max(xs)
best_cost = float('inf')
for xc in range(xmin,xmax+1):
    cost = 0
    for x in xs:
        d = abs(x-xc)
        cost += d*(d+1)//2
    best_cost = min(cost,best_cost)
print(best_cost)
