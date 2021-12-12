print(next(r[0]
    for g in [{}]
    for _ in [[(
        g.update({s : set([t])}) if s not in g else g[s].add(t),
        g.update({t : set([s])}) if t not in g else g[t].add(s)
    ) for l in open('input.txt') for s,t in [l.strip().split('-')]]]
    for r in [[0]]
    for q in [[(set(['start']),'start')]]
    for _ in [[
        r.append(r.pop()+1) if t == 'end' else q.append((v.union([t]) if t == t.lower() else v, t))
        for _ in range(next(a[0] for a in [[1]] for _ in [[a.append(a.pop()*i) for i in range(1,len(g)+1)]]))
        if q for v,s in [q.pop(0)] for t in g[s] if t not in v
    ]]
))
