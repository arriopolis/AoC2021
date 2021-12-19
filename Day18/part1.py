import sys

nums = []
for line in sys.stdin:
    s = line.strip()
    ns,ds = [],[]
    d = 0
    num_str = ''
    for c in s:
        if c == '[':
            d += 1
        elif c == ']':
            if num_str:
                ns.append(int(num_str))
                ds.append(d)
                num_str = ''
            d -= 1
        elif c == ',':
            if num_str:
                ns.append(int(num_str))
                ds.append(d)
                num_str = ''
        else:
            num_str += c
    nums.append((ns,ds))

ns,ds = nums[0]
for ns2,ds2 in nums[1:]:
    ns += ns2
    ds = [d+1 for d in ds] + [d+1 for d in ds2]

    while True:
        # Check for explosion
        for i,((n1,d1),(n2,d2)) in enumerate(zip(list(zip(ns,ds))[:-1], list(zip(ns,ds))[1:])):
            if d1 == d2 and d1 == 5:
                ns[i] = 0
                ds[i] -= 1
                del ns[i+1]
                del ds[i+1]
                if i > 0: ns[i-1] += n1
                if i < len(ns)-1: ns[i+1] += n2
                break
        else:
            # Check for splitting
            for i,(n,d) in enumerate(zip(ns,ds)):
                if n >= 10:
                    l = n//2
                    r = (n+1)//2
                    ns[i] = l
                    ns.insert(i+1,r)
                    ds[i] = d+1
                    ds.insert(i+1, d+1)
                    break
            else:
                break

# Calculate the magnitude
while len(ns) > 1:
    for i,((n1,d1),(n2,d2)) in enumerate(zip(list(zip(ns,ds))[:-1], list(zip(ns,ds))[1:])):
        if d1 == d2:
            ns[i] = 3*n1 + 2*n2
            ds[i] -= 1
            del ns[i+1]
            del ds[i+1]
            break
print(ns[0])
