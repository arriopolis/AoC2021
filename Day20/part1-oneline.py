print(next(sum(sum(r) for r in grid[0]) for lines in [open('input.txt').readlines()] for alg in [lines[0].strip()] for g in [[[1 if c == '#' else 0 for c in line.strip()] for line in lines[2:]]] for n in [2] for grid in [[[[0]*(2*n + len(g)) for _ in range(n)] + [[0]*n + r + [0]*n for r in g] + [[0]*(2*n + len(g)) for _ in range(n)]]] for outside in [[0]] for _ in [[(grid.append([[1 if alg[int(''.join(str(outside[0]) if y+dy < 0 or y+dy >= len(grid[0]) or x+dx < 0 or x+dx >= len(grid[0][0]) else str(grid[0][y+dy][x+dx]) for dy in range(-1,2) for dx in range(-1,2)),2)] == '#' else 0 for x in range(len(grid[0][0]))] for y in range(len(grid[0]))]), grid.pop(0), outside.append(outside.pop() if alg[0] == '.' else 1 - outside.pop())) for _ in range(n)]]))
