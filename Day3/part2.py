import sys

ns = []
for line in sys.stdin:
    ns.append(list(map(int,line.strip())))

# Oxygen
ls = [x.copy() for x in ns]
for i in range(len(ls[0])):
    tokeep = 1 if 2*sum(x[i] for x in ls) >= len(ls) else 0
    ls = list(filter(lambda x : x[i] == tokeep, ls))
    if len(ls) == 1: break
oxygen = int(''.join(map(str,ls[0])),2)

# CO2
ls = [x.copy() for x in ns]
for i in range(len(ls[0])):
    tokeep = 1 if 2*sum(x[i] for x in ls) < len(ls) else 0
    ls = list(filter(lambda x : x[i] == tokeep, ls))
    if len(ls) == 1: break
co2 = int(''.join(map(str,ls[0])),2)

print(oxygen * co2)
