import sys
import heapq

grid = []
for line in sys.stdin:
    grid.append(list(line.rstrip()))

poss = {}
state = []
target_state = []
for i,r in enumerate(grid):
    for j,c in enumerate(r):
        if c == '.' or ord('A') <= ord(c) <= ord('D'):
            poss[(i,j)] = len(state)
            state.append(c)
            target_state.append('.' if i == 1 else chr(ord('A') + (j-3)//2))

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

forbidden = set(poss[(i,j)] for i,j in [(1,3),(1,5),(1,7),(1,9)])
costs = {'A' : 1, 'B' : 10, 'C' : 100, 'D' : 1000}
targets = {'A' : set(), 'B' : set(), 'C' : set(), 'D' : set()}
for ctr in range(len(poss)):
    if target_state[ctr] in targets:
        targets[target_state[ctr]].add(ctr)
hallway = set(poss.values()).difference(set.union(*targets.values()))

lower_bound = 0
for j,c in enumerate(state):
    if c in targets:
        dist = min(dists[j][k] for k in targets[c])
        lower_bound += dist * costs[c]

q = [(lower_bound,0,state)]
visited = set()
while q:
    lb, score, state = heapq.heappop(q)
    if tuple(state) in visited: continue
    if tuple(state) == tuple(target_state):
        print(score)
        break
    visited.add(tuple(state))
    print("Lower bound:", lb, '\t\t\t', "Score:", score)

    # print(f"Investigating the following position (score {score}):")
    # s = [
    #     list('#############'),
    #     list('#...........#'),
    #     list('###.#.#.#.###'),
    #     list('  #.#.#.#.#'),
    #     list('  #########')
    # ]
    # for (i,j),ctr in poss.items():
    #     s[i][j] = state[ctr]
    # print('\n'.join(''.join(r) for r in s))
    # print()
    # import time
    # time.sleep(1)

    for i,c in enumerate(state):
        if c == '.': continue

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
            lower_bound = new_score
            still_to_place = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0}
            for j,d in enumerate(new_state):
                if d in targets:
                    dist = min(dists[j][k] for k in targets[d])
                    lower_bound += dist * costs[d]
                    if j not in targets[d]:
                        still_to_place[d] += 1

            for d,m in still_to_place.items():
                lower_bound += (m-1)*m//2 * costs[d]

            heapq.heappush(q, (lower_bound, new_score, new_state))
