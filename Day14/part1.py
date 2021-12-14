import sys

itr = iter(sys.stdin)
s = list(next(itr).strip())
next(itr)

d = {}
for line in itr:
    lr,m = line.strip().split(' -> ')
    l,r = tuple(lr)
    d[(l,r)] = m

for _ in range(10):
    new_s = [s[0]]
    for a,b in zip(s[:-1],s[1:]):
        new_s.extend([d[(a,b)], b])
    s = new_s

freqs = {}
for c in s:
    if c not in freqs: freqs[c] = 0
    freqs[c] += 1

print(max(freqs.values()) - min(freqs.values()))
