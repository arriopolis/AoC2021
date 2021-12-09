print(next(a*b*c
    for g in [list(map(lambda x : list(map(int,x.strip())), open('input.txt').readlines()))]
    for r in [[[None if g[y][x] == 9 else (y,x) for x in range(len(g[0]))] for y in range(len(g))]]
    for _ in [[
        [
            [
                (
                    r[y].pop(x),
                    r[y].insert(x,m),
                    r[y+dy].pop(x+dx),
                    r[y+dy].insert(x+dx,m)
                )
                for dy,dx in [(-1,0),(0,-1)]
                if 0 <= y+dy < len(g) and 0 <= x+dx < len(g[0]) and r[y+dy][x+dx] is not None and r[y][x] != r[y+dy][x+dx]
                for m in [min(r[y][x],r[y+dy][x+dx])]
            ] for y in range(len(g)) for x in range(len(g[0])) if r[y][x] is not None
        ] for _ in range(len(bin(len(g) * len(g[0]))[2:]))
    ]]
    for d in [{}]
    for _ in [[
        d[r[y][x]].add((y,x)) if r[y][x] in d else d.update({r[y][x] : set([(y,x)])})
        for y in range(len(g)) for x in range(len(g[0])) if r[y][x] is not None
    ]]
    for a,b,c in [sorted(map(len,d.values()), reverse = True)[:3]]
))
