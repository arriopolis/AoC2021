print(next(max(c.values()) - min(c.values())
    for s,p in [open('input.txt').read().strip().split('\n\n')]
    for d in [{(l,r) : m for q in p.split('\n') for lr,m in [q.split(' -> ')] for l,r in [tuple(lr)]}]
    for f in [{}]
    for _ in [[(f.update({(l,r) : 1 if (l,r) not in f else f[(l,r)]+1})) for l,r in zip(s[:-1],s[1:])]]
    for _ in [[(
        f.clear(),
        [
            f.update({
                (l,m) : n if (l,m) not in f else f[(l,m)] + n,
                (m,r) : n if (m,r) not in f else f[(m,r)] + n
            })
            for (l,r),n in g.items() for m in [d[(l,r)]]]
    ) for _ in range(40) for g in [dict(f)]]]
    for c in [{s[0] : 1, s[-1] : 1}]
    for _ in [[(
        c.update({l : n if l not in c else c[l] + n}),
        c.update({r : n if r not in c else c[r] + n})
    ) for (l,r),n in f.items()] + [c.update({l : n//2 for l,n in c.items()})]]
))
