print(next(result[0]
    for grid in [[list(line.rstrip()) for line in open('input.txt')]]
    for hallway,rooms,costs,state,lower_bound,result in [(set(), {'A' : [], 'B' : [], 'C' : [], 'D' : []}, {'A' : 1, 'B' : 10, 'C' : 100, 'D' : 1000}, {}, [0], [float('inf')])]
    for _ in [[(
            hallway.add((y,x)),
            state.update({(y,x) : c})
        ) if c == '.' else (
            rooms[chr(ord('A') + (x-3)//2)].insert(0,(y,x)),
            state.update({(y,x) : c})
        ) if ord('A') <= ord(c) <= ord('D') else None
        for y,r in enumerate(grid) for x,c in enumerate(r)
    ]]
    for _ in [[(
            filled.append([filled.pop(),False][-1]) if state[(y,x)] != c else None,
            (
                lower_bound.append(lower_bound.pop() + (len(ss)-i-1) * costs[c]),
                lower_bound.append(lower_bound.pop() + (len(ss)-i-1) * costs[state[(y,x)]]),
                lower_bound.append(lower_bound.pop() + (dx + 2 if dx > 0 else 4) * costs[state[(y,x)]])
            ) if not filled[0] else None
        )
        for c,ss in rooms.items()
        for filled in [[True]]
        for i,(y,x) in enumerate(ss)
        for dx in [abs(3 + 2*(ord(state[(y,x)]) - ord('A')) - x)]
    ]]
    for q,visited in [({lower_bound[0] : set([(0,tuple(sorted(state.items())))])}, set())]
    for _ in [[None
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for _ in range(2) if q
        for m in [min(q.keys())]
        for _ in [[None
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for _ in range(2) if m in q and q[m]
            for const_score,const_state in [q[m].pop()]
            for score in [[const_score]]
            for state in [dict(const_state)]
            for lb in [m]
            for _ in [[None
                for changed in [[True]]
                for _ in range(2) if changed[0]
                for _ in range(2) if changed[0]
                for _ in range(2) if changed[0]
                for _ in range(2) if changed[0]
                for _ in [changed.append([changed.pop(), False][-1])]
                for c,ss in rooms.items()
                for busy in [[True]]
                for y,x in ss
                if busy[0] and state[(y,x)] != c
                for _ in [busy.append([busy.pop(),False][-1])]
                if all(state[(y2,x)] == '.' for y2 in range(y,1,-1))
                for y2 in [[y]]
                for i in [range(x+1,12),range(x-1,0,-1)]
                for busy2 in [[True]]
                for x2 in i
                if busy2[0]
                for _ in [(
                        state.update({(y2[0],x) : c, (1,x2) : '.'}),
                        score.append(score.pop() + (y2[0]-1 + abs(x2-x)) * costs[c]),
                        y2.append(y2.pop() - 1),
                        changed.append([changed.pop(), True][-1])
                    ) if state[(1,x2)] == c else [(
                            state.update({(y2[0],x) : c, (y3,x2) : '.'}),
                            score.append(score.pop() + (y3-1 + y2[0]-1 + abs(x2-x)) * costs[c]),
                            y2.append(y2.pop() - 1),
                            changed.append([changed.pop(), True][-1])
                        ) if state[(y3,x2)] == c else
                        busy3.append([busy3.pop(), False][-1])
                        if state[(y3,x2)] != '.' else None
                        for busy3 in [[True]]
                        for y3 in range(2,len(grid)-1)
                        if busy3[0]
                    ] if 3 <= x2 <= 9 and x2%2 == 1 else
                    busy2.append([busy2.pop(), False][-1])
                    if state[(1,x2)] != '.' else None
                ]
            ]]
            for _ in [
                (result.clear(), result.append(m), q.clear())
                if all(all(state[(y,x)] == c for y,x in ss) for c,ss in rooms.items()) else
                None
            ]
            if tuple(sorted(state.items())) not in visited
            for _ in [visited.add(tuple(sorted(state.items())))]
            for _ in [[
                q.update({new_lb : set([(new_score,tuple(sorted(new_state.items())))])})
                if new_lb not in q else
                q[new_lb].add((new_score,tuple(sorted(new_state.items()))))
                for t,ss in rooms.items()
                for busy in [[True]]
                for y,x in reversed(ss)
                if busy[0] and state[(y,x)] != '.'
                for _ in [busy.append([busy.pop(), False][-1])]
                if not all(state[(y2,x)] == t for y2 in range(y,len(grid)-1))
                for c in [state[(y,x)]]
                for i in [range(x+1,12), range(x-1,0,-1)]
                for busy2 in [[True]]
                for x2 in i
                if not (3 <= x2 <= 9 and x2%2 == 1)
                for _ in [busy2.append([busy2.pop(), False][-1]) if state[(1,x2)] != '.' else None]
                if busy2[0]
                for target_x in [3 + 2*(ord(c) - ord('A'))]
                if all(
                    abs(target_x2-x2) + abs(x2-x3) + abs(x3-target_x) != abs(target_x2-target_x)
                    for x3 in range(x2,target_x,2 if target_x > x2 else -2)
                    if state[(1,x3)] != '.'
                    for d in [state[(1,x3)]]
                    for target_x2 in [3 + 2*(ord(d) - ord('A'))]
                )
                for new_state in [state.copy()]
                for _ in [new_state.update({(1,x2) : c, (y,x) : '.'})]
                for new_score in [score[0] + (y-1 + abs(x-x2)) * costs[c]]
                for new_lb in [lb + (abs(x-x2)+abs(x2-target_x)-max(abs(x-target_x),2)) * costs[c]]
            ]]
        ]]
        for _ in [q.pop(m) if m in q else None]
    ]]
))
