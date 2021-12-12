import sys

graph = {}
for line in sys.stdin:
    s,t = line.strip().split('-')
    if s not in graph: graph[s] = set()
    graph[s].add(t)
    if t not in graph: graph[t] = set()
    graph[t].add(s)

def DFS(visited, s):
    if s == 'end': return 1
    res = 0
    for t in graph[s]:
        if t in visited: continue
        new_visited = visited.union(set([t])) if t == t.lower() else visited
        res += DFS(new_visited, t)
    return res

print(DFS(set(['start']), 'start'))
