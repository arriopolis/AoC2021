print(next(ns[0]
    for nums in [[(ns,ds)
        for line in open('input.txt')
        for ns,ds,d,num_str in [([],[],[0],[''])]
        for _ in [[
            d.append(d.pop()+1) if c == '[' else
            (
                (ns.append(int(num_str.pop())), ds.append(d[0]), num_str.append('')) if num_str[0] else None,
                d.append(d.pop()-1)
            ) if c == ']' else
            (ns.append(int(num_str.pop())), ds.append(d[0]), num_str.append('')) if num_str[0] else None if c == ',' else
            num_str.append(num_str.pop() + c)
            for c in line.strip()
        ]]
    ]]
    for ns,ds in [nums[0]]
    for _ in [[(
            ns.extend(ns2),
            ds.extend(ds2),
            [ds.insert(i,ds.pop(i)+1) for i in range(len(ds))],
            [
                [
                    (
                        ns.insert(i-1, ns.pop(i) + ns.pop(i-1)) if i > 0 else ns.pop(0),
                        ns.insert(i,0),
                        ns.insert(i+1, ns.pop(i+2) + ns.pop(i+1)) if i < len(ns)-2 else ns.pop(i+1),
                        ds.insert(i, ds.pop(i)-1),
                        ds.pop(i+1)
                    ) for i in [ds.index(5)]
                ] if 5 in ds else [
                    (
                        ns.pop(i),
                        ns.insert(i,l),
                        ns.insert(i+1,r),
                        ds.insert(i,ds.pop(i)+1),
                        ds.insert(i+1,ds[i])
                    )
                    for i in [min(i for i,n in enumerate(ns) if n >= 10)]
                    for l,r in [(ns[i]//2,(ns[i]+1)//2)]
                ] if any(n >= 10 for n in ns) else None
                for _ in range(len(ns)**2)
            ]
        ) for ns2,ds2 in nums[1:]
    ]]
    for _ in [[
        (
            ns.insert(i, 2*ns.pop(i+1) + 3*ns.pop(i)),
            ds.insert(i, ds.pop(i) - 1),
            ds.pop(i+1)
        )
        for _ in range(len(ns)-1)
        for i in [min(i for i,(d1,d2) in enumerate(zip(ds[:-1],ds[1:])) if d1 == d2)]
    ]]
))
