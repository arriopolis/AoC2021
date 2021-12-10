print(next(sorted(t)[len(t)//2]
    for p in [{'(' : ')', '[' : ']', '{' : '}', '<' : '>'}]
    for s in [{')' : 1, ']' : 2, '}' : 3, '>' : 4}]
    for t in [[x[0]
        for line in open('input.txt')
        for q in [[]]
        for r in [[]]
        for _ in [[q.append(c) if c in '([{<' else r.append(c) if not q or p[q[-1]] != c else q.pop() for c in line.strip() if not r]]
        if not r
        for x in [[0]]
        for _ in [[x.append(x.pop() * 5 + s[p[c]]) for c in reversed(q)]]
    ]]
))
