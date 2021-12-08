import sys

nums = {
    'abcefg' : 0,
    'cf' : 1,
    'acdeg' : 2,
    'acdfg' : 3,
    'bcdf' : 4,
    'abdfg' : 5,
    'abdefg' : 6,
    'acf' : 7,
    'abcdefg' : 8,
    'abcdfg' : 9
}

ns = []
for line in sys.stdin:
    a,b = line.strip().split(' | ')

    lendict = {}
    len6dict = {}
    set2 = set()
    set3 = set()
    for s in a.split():
        if len(s) == 2: set2.update(s)
        if len(s) == 3: set3.update(s)
        if len(s) == 6:
            for c in s:
                if c not in len6dict: len6dict[c] = 0
                len6dict[c] += 1
        for c in s:
            if c not in lendict: lendict[c] = 0
            lendict[c] += 1

    d = {}
    d[set3.difference(set2).pop()] = 'a'
    for k,v in lendict.items():
        if v == 9: d[k] = 'f'
        if v == 4: d[k] = 'e'
        if v == 6: d[k] = 'b'
        if v == 8 and k not in d: d[k] = 'c'
    for k,v in len6dict.items():
        if v == 2 and k not in d: d[k] = 'd'
        if v == 3 and k not in d: d[k] = 'g'

    ns.append(int(''.join(str(nums[''.join(sorted(d[c] for c in x))]) for x in b.split())))
print(sum(ns))
