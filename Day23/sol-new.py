import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.rstrip()))

hallway = set()
rooms = {'A' : [], 'B' : [], 'C' : [], 'D' : []}
state = {}
for y,r in enumerate(grid):
    for x,c in enumerate(r):
        if c == '.':
            hallway.add((y,x))
            state[(y,x)] = c
        elif ord('A') <= ord(c) <= ord('D'):
            rooms[chr(ord('A') + (x-3)//2)].insert(0,(y,x))
            state[(y,x)] = c

costs = {'A' : 1, 'B' : 10, 'C' : 100, 'D' : 1000}
lower_bound = 0
for c,ss in rooms.items():
    filled = True
    for i,(y,x) in enumerate(ss):
        if state[(y,x)] != c:
            filled = False
        if not filled:
            # Cost of filling this place
            lower_bound += (len(ss)-i-1) * costs[c]
            # Cost of moving to the edge of the room
            lower_bound += (len(ss)-i-1) * costs[state[(y,x)]]
            # Cost of moving over to the correct room
            dx = abs(3 + 2*(ord(state[(y,x)]) - ord('A')) - x)
            lower_bound += (dx + 2 if dx > 0 else 4) * costs[state[(y,x)]]

q = {lower_bound : set([(0,tuple(sorted(state.items())))])}
visited = set()
while q:
    m = min(q.keys())
    while q[m]:
        score, const_state = q[m].pop()
        state = dict(const_state)
        lb = m

        # Perform provably optimal moves
        changed = True
        while changed:
            changed = False
            for c,ss in rooms.items():
                for y,x in ss:
                    if state[(y,x)] == c: continue
                    for y2 in range(y,1,-1):
                        if state[(y2,x)] != '.': break
                    else:
                        for i in [range(x+1,12),range(x-1,0,-1)]:
                            for x2 in i:
                                if state[(1,x2)] == c:
                                    state[(y,x)] = c
                                    state[(1,x2)] = '.'
                                    score += (y-1 + abs(x2-x)) * costs[c]
                                    y -= 1
                                    changed = True
                                elif state[(1,x2)] != '.': break
                                if 3 <= x2 <= 9 and x2%2 == 1:
                                    for y2 in range(2,len(grid)-1):
                                        if state[(y2,x2)] == c:
                                            state[(y,x)] = c
                                            state[(y2,x2)] = '.'
                                            score += (y2-1 + y-1 + abs(x2-x)) * costs[c]
                                            y -= 1
                                            changed = True
                                        elif state[(y2,x2)] != '.': break
                    break


        for c,ss in rooms.items():
            for y,x in ss:
                if state[(y,x)] != c:
                    break
            else: continue
            break
        else:
            print(score)
            break

        # Check if we have visited this state before
        const_state = tuple(sorted(state.items()))
        if const_state in visited: continue
        visited.add(const_state)

        # Find the possible moves
        for t,ss in rooms.items():
            for y,x in reversed(ss):
                if state[(y,x)] == '.': continue
                if state[(y,x)] == t:
                    for y2 in range(y+1,len(grid)-1):
                        if state[(y2,x)] != t: break
                    else: break

                c = state[(y,x)]
                for i in [range(x+1,12),range(x-1,0,-1)]:
                    for x2 in i:
                        if 3 <= x2 <= 9 and x2%2 == 1: continue
                        if state[(1,x2)] != '.': break

                        # Check if there is an obstruction
                        target_x = 3 + 2*(ord(c) - ord('A'))
                        for x3 in range(x2,target_x,2 if target_x > x2 else -2):
                            if state[(1,x3)] != '.':
                                d = state[(1,x3)]
                                target_x2 = 3 + 2*(ord(d) - ord('A'))
                                if abs(target_x2-x2) + abs(x2-x3) + abs(x3-target_x) == abs(target_x2-target_x):
                                    break
                        else:
                            # Modify the state
                            new_state = state.copy()
                            new_state[(1,x2)] = c
                            new_state[(y,x)] = '.'
                            new_score = score + (y-1 + abs(x-x2)) * costs[c]
                            new_lb = lb + (abs(x-x2)+abs(x2-target_x)-max(abs(x-target_x),2)) * costs[c]

                            # Check if the new state can be easily refuted
                            num_remove = 0
                            non_fixed = False
                            for y3,x3 in rooms[c]:
                                if new_state[(y3,x3)] != c: non_fixed = True
                                if new_state[(y3,x3)] == '.': break
                                if non_fixed: num_remove += 1

                            moves = [False,False]
                            num_room_empty = 0
                            nums = [0,0]
                            nums_empty = [0,0]
                            for j,k in enumerate([range(3+2*(ord(c)-ord('A'))-1,0,-1),range(3+2*(ord(c)-ord('A'))+1,12)]):
                                for x3 in k:
                                    if new_state[(1,x3)] == c:
                                        moves[j] = True
                                        break
                                    if 3 <= x3 <= 9 and x3%2 == 1:
                                        for y4,x4 in reversed(rooms[chr(ord('A') + (x3-3)//2)]):
                                            if new_state[(y4,x4)] != '.': break
                                            num_room_empty += 1
                                    elif new_state[(1,x3)] != '.':
                                        nums[j] += 1
                                    else:
                                        nums_empty[j] += 1

                            if moves[0] and moves[1]:
                                if num_room_empty + nums_empty[1] < num_remove + nums[0] and num_room_empty + nums_empty[0] < num_remove + nums[1]:
                                    continue
                            elif moves[0]:
                                if num_room_empty + nums_empty[1] < num_remove + nums[0]:
                                    continue
                            elif moves[1]:
                                if num_room_empty + nums_empty[0] < num_remove + nums[1]:
                                    continue

                            # Store the option
                            if new_lb not in q: q[new_lb] = set()
                            q[new_lb].add((new_score,tuple(sorted(new_state.items()))))
                break
    else:
        del q[m]
        continue
    break
