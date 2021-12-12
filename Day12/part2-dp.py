import sys

graph = {}
for line in sys.stdin:
    s,t = line.strip().split('-')
    if s not in graph: graph[s] = set()
    graph[s].add(t)
    if t not in graph: graph[t] = set()
    graph[t].add(s)

new_graph = {}
for s in graph:
    if s != s.lower(): continue
    new_graph[s] = {}
    for t in graph[s]:
        if t == t.lower():
            if t not in new_graph[s]: new_graph[s][t] = 0
            new_graph[s][t] += 1
        else:
            for u in graph[t]:
                if u not in new_graph[s]: new_graph[s][u] = 0
                new_graph[s][u] += 1

dp = {(tuple(),None,'start') : 1}
q = [(tuple(),None,'start')]
tot = 0
while q:
    visited, dbl, s = q.pop(0)
    for t,n in new_graph[s].items():
        if t == 'end':
            tot += dp[(visited,dbl,s)] * n
            continue
        if t == 'start': continue
        if t in visited and dbl is not None: continue
        new_dbl = t if t in visited else dbl
        new_visited = tuple(sorted(visited + (t,))) if t not in visited else visited
        if (new_visited,new_dbl,t) not in dp:
            dp[(new_visited,new_dbl,t)] = 0
            q.append((new_visited,new_dbl,t))
        dp[(new_visited,new_dbl,t)] += dp[(visited,dbl,s)] * n
print(tot)
