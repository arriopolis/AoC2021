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
    for d in [{(tuple(),'start') : 1}]
    for q in [[(tuple(),'start')]]
    for r in [[0]]
    for _ in [[
        r.append(r.pop() + d[(v,s)]*n)
        if t == 'end' else
        (d.update({(w,t) : d[(v,s)]*n}), q.append((w,t)))
        if (w,t) not in d else
        d.update({(w,t) : d[(w,t)] + d[(v,s)]*n})
        for _ in range(2**len(h) * len(h)) if q
        for v,s in [q.pop(0)] for t,n in h[s].items()
        if t != 'start' if t not in v for w in [tuple(sorted(v + (t,)))]
    ]]
))
