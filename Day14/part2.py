import sys

itr = iter(sys.stdin)
s = list(next(itr).strip())
next(itr)

d = {}
for line in itr:
    lr,m = line.strip().split(' -> ')
    l,r = tuple(lr)
    d[(l,r)] = m

freqs = {}
for l,r in zip(s[:-1],s[1:]):
    if (l,r) not in freqs: freqs[(l,r)] = 0
    freqs[(l,r)] += 1

for _ in range(40):
    new_freqs = {}
    for (l,r),n in freqs.items():
        m = d[(l,r)]
        if (l,m) not in new_freqs: new_freqs[(l,m)] = 0
        new_freqs[(l,m)] += n
        if (m,r) not in new_freqs: new_freqs[(m,r)] = 0
        new_freqs[(m,r)] += n
    freqs = new_freqs

char_freqs = {}
for (l,r),n in freqs.items():
    if l not in char_freqs: char_freqs[l] = 0
    char_freqs[l] += n
    if r not in char_freqs: char_freqs[r] = 0
    char_freqs[r] += n
char_freqs[s[0]] += 1
char_freqs[s[-1]] += 1
char_freqs = {c : n//2 for c,n in char_freqs.items()}

print(max(char_freqs.values()) - min(char_freqs.values()))
