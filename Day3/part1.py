import sys

ns = []
for line in sys.stdin:
    ns.append(list(map(int,line.strip())))

transpose = list(zip(*ns))
eps = ''
gamma = ''
for x in transpose:
    eps += '1' if 2*sum(x) > len(x) else '0'
    gamma += '0' if 2*sum(x) > len(x) else '1'
eps = int(eps,2)
gamma = int(gamma,2)
print(eps * gamma)
