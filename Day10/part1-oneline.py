print(sum(s[r[0]] for p in [{'(' : ')', '[' : ']', '{' : '}', '<' : '>'}] for s in [{')' : 3, ']' : 57, '}' : 1197, '>' : 25137}] for line in open('input.txt') for q in [[]] for r in [[]] for _ in [[q.append(c) if c in '([{<' else r.append(c) if not q or p[q[-1]] != c else q.pop() for c in line.strip() if not r]] if r))