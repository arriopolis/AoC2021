print(next(sum(abs(y-m)*(abs(y-m)+1)//2 for y in z) for z in [list(map(int,open('input.txt').read().split(',')))] for m in [(2*sum(z)+1)//(2*len(z))]))
