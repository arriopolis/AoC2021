print(next(r[-1][-1]
    for g in [[sum(([(int(c)+i-1)%9+1 for c in l.strip()] for i in range(5)),[]) for l in open('input.txt')]]
    for _ in [[g.extend([[(c+i)%9+1 for c in l] for l in g[:h]]) for h in [len(g)] for i in range(4)]]
    for r in [[[float('inf')]*len(g[0]) for _ in g]]
    for _ in [(r[0].pop(0),r[0].insert(0,0))]
    for d in [{0 : set([(0,0)])}]
    for _ in [[
        (
            r[y+dy].pop(x+dx),
            r[y+dy].insert(x+dx,n),
            d[n].add((y+dy,x+dx)) if n in d else d.update({n : set([(y+dy,x+dx)])})
        )
        for k in range(9*len(g)*len(g[0])+1) if k in d
        for y,x in d[k] if r[y][x] == k for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]
        if 0 <= y+dy < len(g) and 0 <= x+dx < len(g[0]) and r[y+dy][x+dx] > r[y][x] + g[y+dy][x+dx]
        for n in [r[y][x] + g[y+dy][x+dx]]
    ]]
))
