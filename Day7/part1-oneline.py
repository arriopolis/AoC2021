print(next(sum(abs(y-z[len(z)//2]) for y in z) for z in [sorted(map(int,open('input.txt').read().split(',')))]))
