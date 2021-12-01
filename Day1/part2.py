import sys
ns = []
for line in sys.stdin:
    ns.append(int(line))

ctr = 0
for i in range(len(ns)-3):
    a = ns[i] + ns[i+1] + ns[i+2]
    b = ns[i+1] + ns[i+2] + ns[i+3]
    if a < b:
        ctr += 1
print(ctr)
