print(next(sum(a<b for a,b in zip(y[:-1],y[1:])) for x in [list(map(int, open('input.txt').readlines()))] for y in [[a+b+c for a,b,c in zip(x[:-2],x[1:-1],x[2:])]]))
