import sys
xs = sorted(map(int,sys.stdin.read().strip().split(',')))
x = xs[len(xs)//2]
print(sum(abs(y-x) for y in xs))
