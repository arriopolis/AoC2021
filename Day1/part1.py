import sys
ns = []
for line in sys.stdin:
    ns.append(int(line))

ctr = 0
for a,b in zip(ns[:-1],ns[1:]):
    if a < b:
        ctr += 1
print(ctr)
