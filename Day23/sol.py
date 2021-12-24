import sys
import heapq

grid = []
for line in sys.stdin:
    grid.append(list(line.rstrip()))

poss = {}
state = []
for i,r in enumerate(grid):
    for j,c in enumerate(r):
        if c == '.' or ord('A') <= ord(c) <= ord('D'):
            poss[(i,j)] = len(state)
            state.append(c)

neighbors = [set() for _ in poss]
for (i,j),ctr in poss.items():
    for dy,dx in [(-1,0),(0,-1),(1,0),(0,1)]:
        y,x = i+dy,j+dx
        if 0 <= y < len(grid) and 0 <= x < len(grid[y]) and (grid[y][x] == '.' or ord('A') <= ord(grid[y][x]) <= ord('D')):
            neighbors[ctr].add(poss[(y,x)])

dists = [[float('inf') if i != j else 0 for j in range(len(poss))] for i in range(len(poss))]
for _ in range(len(poss)):
    for i,s in enumerate(neighbors):
        for j in s:
            for k in range(len(neighbors)):
                if dists[k][i] + 1 < dists[k][j]:
                    dists[k][j] = dists[k][i] + 1
                    dists[j][k] = dists[k][j]

costs = {'A' : 1, 'B' : 10, 'C' : 100, 'D' : 1000}
forbidden = set(poss[(i,j)] for i,j in [(1,3),(1,5),(1,7),(1,9)])
targets = {
    'A' : [poss[(i,3)] for i in range(len(grid)-2,1,-1)],
    'B' : [poss[(i,5)] for i in range(len(grid)-2,1,-1)],
    'C' : [poss[(i,7)] for i in range(len(grid)-2,1,-1)],
    'D' : [poss[(i,9)] for i in range(len(grid)-2,1,-1)]
}
hallway = set(poss.values()).difference(set.union(*map(set,targets.values())))

def lower_bound(state):
    lb = 0
    for c,l in targets.items():
        filled = True
        for n in l:
            if state[n] != c:
                filled = False
            if not filled:
                if state[n] != '.': lb += dists[n][targets[state[n]][-1]] * costs[state[n]]
                if state[n] == c: lb += costs[c] * 4
                lb += dists[n][targets[c][-1]] * costs[c]

    for n in hallway:
        if state[n] == '.': continue
        lb += dists[n][targets[state[n]][-1]] * costs[state[n]]

    return lb

def solved(state):
    for c,l in targets.items():
        for n in l:
            if state[n] != c: return False
    return True

def print_state(state, score):
    print(f"Investigating the following position (score {score}):")
    s = [
        list('#############'),
        list('#...........#'),
        list('###.#.#.#.###'),
        list('  #.#.#.#.#'),
        list('  #########')
    ]
    for (i,j),ctr in poss.items():
        s[i][j] = state[ctr]
    print('\n'.join(''.join(r) for r in s))
    print()

lb = lower_bound(state)
q = [(lb,0,state)]
visited = set()
while q:
    lb, score, state = heapq.heappop(q)
    if tuple(state) in visited: continue
    visited.add(tuple(state))
    # print("Lower bound:", lb, '\t\t\t', "Score:", score)

    # print_state(state, score)

    # Immediately perform moves that are provably optimal
    while True:
        for i,c in enumerate(state):
            if c == '.': continue
            if i in targets[c] and all(state[n] == c for n in targets[c][:targets[c].index(i)]): continue

            frontier = set([i])
            been = set()
            m = 1
            while frontier:
                new_frontier = set()
                for j in frontier:
                    been.add(j)
                    for k in neighbors[j]:
                        if state[k] != '.': continue
                        if k in been: continue
                        if k in targets[c] and all(state[n] == c for n in targets[c][:targets[c].index(k)]):
                            state[i] = '.'
                            state[k] = c
                            score += costs[c] * m
                            break
                        new_frontier.add(k)
                    else: continue
                    break
                else:
                    frontier = new_frontier
                    m += 1
                    continue
                break
            else: continue
            break
        else: break

    if solved(state):
        print(score)
        break

    for i,c in enumerate(state):
        if c == '.': continue
        if i in targets[c] and all(state[n] == c for n in targets[c][:targets[c].index(i)]): continue

        moves = {}
        frontier = set([i])
        m = 0
        while frontier:
            new_frontier = set()
            for j in frontier:
                moves[j] = m
                for k in neighbors[j]:
                    if state[k] != '.': continue
                    if k in moves: continue
                    new_frontier.add(k)
            frontier = new_frontier
            m += 1

        for j,m in moves.items():
            # Check if the move is valid
            if j in forbidden or i == j: continue
            if i in hallway and j not in targets[c]: continue
            if i not in hallway and j not in hallway: continue
            if i in hallway and any(state[sq] not in c + '.' for sq in targets[c]): continue

            new_score = score + m * costs[c]
            new_state = state.copy()
            new_state[j] = c
            new_state[i] = '.'
            if tuple(new_state) in visited: continue

            # Compute lower bound
            lb = new_score + lower_bound(new_state)

            heapq.heappush(q, (lb, new_score, new_state))
