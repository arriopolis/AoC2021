print(next(r[0][1][0]
    for b in [sum((list(map(int,bin(int(c,16))[2:].zfill(4))) for c in open('input.txt').read().strip()), [])]
    for p in [[0]]
    for r in [[(None,[])]]
    for w in [[]]
    for _ in [[
        (
            (
                r[-2][1].append(int(''.join(map(str,r.pop())),2)),
                w.pop(),
            ) if w[-1][1] == 0 else
            (
                r[-1].extend(b[p[0]+1:p[0]+5]),
                w[-1].pop(),
                w[-1].append(b[p[0]]),
                p.append(p.pop()+5)
            )
        ) if w and w[-1][0] == 0 else
        next(
            (r[-1][1].append(
                sum(l) if t == 0 else
                [y[0] for y in [[1]] for x in l for _ in [y.append(y.pop()*x)]][-1] if t == 1 else
                min(l) if t == 2 else
                max(l) if t == 3 else
                int(l[0] > l[1]) if t == 5 else
                int(l[0] < l[1]) if t == 6 else
                int(l[0] == l[1])
            ),w.pop()) for t,l in [r.pop()]
        )
        if w and (
            (w[-1][0] == 1 and w[-1][1] == p[0])
            or (w[-1][0] == 2 and w[-1][1] == len(r[-1][1]))
        ) else
        next(
            (
                r.append([]),
                w.append([0,1]),
                p.append(p.pop()+6),
            ) if t == 4 else
            (
                r.append((t,[])),
                next(
                    (
                        w.append((1,p[0]+22+int(''.join(map(str,b[p[0]+7:p[0]+22])),2))),
                        p.append(p.pop()+22)
                    ) if u == 0 else
                    (
                        w.append((2,int(''.join(map(str,b[p[0]+7:p[0]+18])),2))),
                        p.append(p.pop()+18)
                    ) for u in [b[p[0]+6]]
                ),
            ) for t in [int(''.join(map(str,b[p[0]+3:p[0]+6])),2)]
        ) for _ in b if not r[0][1]
    ]]
))
