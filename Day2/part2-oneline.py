print(next(c*d for a in [[0]] for c,d in [list(map(sum, zip(*map(lambda x : [(0,0),a.append(a.pop()+int(x[1]))][0] if x[0] == 'down' else [(0,0),a.append(a.pop()-int(x[1]))][0] if x[0] == 'up' else (int(x[1]),int(x[1])*a[0]), map(lambda x : x.strip().split(), open('input.txt').readlines())))))]))
