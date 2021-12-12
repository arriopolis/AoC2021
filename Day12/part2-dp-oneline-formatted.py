print(next(r[0]
    for g in [{}]
    for _ in [[(
        g.update({s : set([t])}) if s not in g else g[s].add(t),
        g.update({t : set([s])}) if t not in g else g[t].add(s)
    ) for l in open('input.txt') for s,t in [l.strip().split('-')]]]
    for h in [{s : {} for s in g if s == s.lower()}]
    for _ in [[
        (
            h[s].update({t:1 if t not in h[s] else h[s][t]+1})
            if t == t.lower() else
            [h[s].update({u:1 if u not in h[s] else h[s][u]+1}) for u in g[t]]
        ) for s in g if s == s.lower() for t in g[s]
    ]]
    for d in [{(tuple(),None,'start') : 1}]
    for q in [[(tuple(),None,'start')]]
    for r in [[0]]
    for _ in [[
        r.append(r.pop() + d[(v,m,s)]*n)
        if t == 'end' else
        (d.update({(w,l,t) : d[(v,m,s)]*n}), q.append((w,l,t)))
        if (w,l,t) not in d else
        d.update({(w,l,t) : d[(w,l,t)] + d[(v,m,s)]*n})
        for _ in range(2**len(h) * len(h)**2) if q
        for v,m,s in [q.pop(0)] for t,n in h[s].items()
        if t != 'start' if (t not in v or m is None)
        for w in [tuple(sorted(v + (t,)))] for l in [t if t in v else m]
    ]]
))
