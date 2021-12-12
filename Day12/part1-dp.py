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

dp = {(tuple(['start']),'start') : 1}
q = [(tuple(['start']),'start')]
tot = 0
while q:
    visited, s = q.pop(0)
    for t,n in new_graph[s].items():
        if t in visited: continue
        if t == 'end':
            tot += dp[(visited,s)] * n
            continue
        new_visited = tuple(sorted(visited + (t,)))
        if (new_visited,t) not in dp:
            dp[(new_visited,t)] = 0
            q.append((new_visited,t))
        dp[(new_visited,t)] += dp[(visited,s)] * n
print(tot)
