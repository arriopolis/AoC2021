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
        new_visited = visited.copy()
        if t == t.lower():
            if t not in new_visited: new_visited[t] = 0
            new_visited[t] += 1
            if new_visited['start'] == 2: continue
            l = sorted(list(new_visited.values()), reverse = True)
            if len(l) >= 2 and (l[0] > 2 or l[1] >= 2): continue
        res += DFS(new_visited, t)
    return res

print(DFS({'start' : 1}, 'start'))
