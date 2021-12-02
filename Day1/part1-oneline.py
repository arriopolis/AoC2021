print(next(sum(a<b for a,b in zip(x[:-1],x[1:])) for x in [list(map(int, open('input.txt').readlines()))]))
