print(next(sum(int(m[0])
        for k in range(min(a,0),max(0,b)+1) for l in range(-max(abs(c),abs(d)+1), max(abs(c),abs(d)+1))
        for x,y,vx,vy,m in [([0],[0],[k],[l],[False])]
        for _ in [[(
            x.append(x.pop()+vx[0]),
            y.append(y.pop()+vy[0]),
            n.append(max(n.pop(),y[0])),
            vx.append(vx.pop()-1 if vx[0] > 0 else vx.pop()+1 if vx[0] < 0 else vx.pop()),
            vy.append(vy.pop()-1),
            m.append(m.pop() or True) if a <= x[0] <= b and c <= y[0] <= d else None
        ) for n in [[0]] for t in range((-2*c+abs(2*l+1)-1)//abs(2*l+1) + max((2*l+1),0))]]
    ) for (a,b),(c,d) in [[[int(c) for c in z.split('=')[1].split('..')] for z in open('input.txt').read().strip()[13:].split(', ')]]
))
