print(next(ctr[0]
    for grid in [[list(line.strip()) for line in open('input.txt')]]
    for h,w in [(len(grid),len(grid[0]))]
    for changed in [[True]]
    for ctr in [[0]]
    for _ in [[
        None
        for _ in range(2) if changed[0]
        for _ in range(2) if changed[0]
        for _ in range(2) if changed[0]
        for _ in range(2) if changed[0]
        for _ in range(2) if changed[0]
        for _ in range(2) if changed[0]
        for _ in range(2) if changed[0]
        for _ in range(2) if changed[0]
        for _ in range(2) if changed[0]
        for _ in [(changed.pop(), changed.append(False))]
        for _ in [ctr.append(ctr.pop() + 1)]
        for to_move in [set()]
        for _ in [[
            (
                to_move.add(((i,j),(i,(j+1)%w))),
                changed.pop(),
                changed.append(True)
            )
            for i in range(h)
            for j in range(w)
            if grid[i][j] == '>' and grid[i][(j+1)%w] == '.'
        ]]
        for _ in [[
            (
                grid[i2].pop(j2),
                grid[i2].insert(j2, c),
                grid[i].pop(j),
                grid[i].insert(j, '.')
            )
            for (i,j),(i2,j2) in to_move
            for c in [grid[i][j]]
        ]]
        for _ in [to_move.clear()]
        for _ in [[
            (
                to_move.add(((i,j),((i+1)%h,j))),
                changed.pop(),
                changed.append(True)
            )
            for j in range(w)
            for i in range(h)
            if grid[i][j] == 'v' and grid[(i+1)%h][j] == '.'
        ]]
        for _ in [[
            (
                grid[i2].pop(j2),
                grid[i2].insert(j2, c),
                grid[i].pop(j),
                grid[i].insert(j, '.')
            )
            for (i,j),(i2,j2) in to_move
            for c in [grid[i][j]]
        ]]
    ]]
))
