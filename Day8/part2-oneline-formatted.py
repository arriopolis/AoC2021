print(sum(int(''.join(str(n[''.join(sorted(d[c] for c in x))]) for x in b.split()))
    for n in [{'abcefg' : 0, 'cf' : 1, 'acdeg' : 2, 'acdfg' : 3, 'bcdf' : 4, 'abdfg' : 5, 'abdefg' : 6, 'acf' : 7, 'abcdefg' : 8, 'abcdfg' : 9}]
    for line in open('input.txt').readlines()
    for a,b in [line.strip().split(' | ')]
    for l,m,s,t,d in [({},{},set(),set(),{})]
    for _ in [[
        (
            [l.update({c : l[c]+1 if c in l else 1}) for c in x],
            [m.update({c : m[c]+1 if c in m else 1}) for c in x] if len(x) == 6 else
            s.update(x) if len(x) == 2 else
            t.update(x) if len(x) == 3 else
            None
        )
        for x in a.split()
    ]]
    for _ in [d.update({t.difference(s).pop() : 'a'})]
    for _ in [[
        d.update({k : 'f'}) if v == 9 else
        d.update({k : 'e'}) if v == 4 else
        d.update({k : 'b'}) if v == 6 else
        d.update({k : 'c'}) if v == 8 and k not in d else
        None
        for k,v in l.items()
    ]]
    for _ in [[
        d.update({k : 'd'}) if v == 2 and k not in d else
        d.update({k : 'g'}) if v == 3 and k not in d else
        None
        for k,v in m.items()
    ]]
))
