print(next(max(abs(x2-x1) + abs(y2-y1) + abs(z2-z1)
        for i,(x1,y1,z1) in poss.items()
        for j,(x2,y2,z2) in poss.items()
        if i != j
    )
    for beacons,scanners in [([[]],[])]
    for _ in [[
        (beacons.pop(),beacons.append([]),scanners.append(beacons[0]))
        if line[:3] == '---' else
        beacons[0].append(tuple(map(int,line.strip().split(','))))
        for line in open('input.txt') if line.strip()
    ]]
    for grid,poss,locs,diffs in [(set(scanners[0]), {0 : (0,0,0)}, {0 : {}}, {0 : {}})]
    for _ in [[locs[0].update({i : (x,y,z)}) for i,(x,y,z) in enumerate(scanners[0])]]
    for _ in [[diffs[0][i].add(diff)
        for i,(x1,y1,z1) in enumerate(scanners[0])
        for _ in [diffs[0].update({i : set()})]
        for j,(x2,y2,z2) in enumerate(scanners[0])
        if i != j
        for diff in [(x2-x1,y2-y1,z2-z1)]
    ]]
    for _ in [[(
            [new_diffs[i].add(diff)
                for i,(x1,y1,z1) in enumerate(rbs[0])
                for _ in [new_diffs.update({i : set()})]
                for j,(x2,y2,z2) in enumerate(rbs[0])
                if i != j
                for diff in [(x2-x1,y2-y1,z2-z1)]
            ],
            [(
                poss.update({s : (pos_x,pos_y,pos_z)}),
                diffs.update({s : new_diffs}),
                locs.update({s : {}}),
                [(locs[s].update({i : (new_x,new_y,new_z)}),grid.add((new_x,new_y,new_z)))
                    for i,(x,y,z) in enumerate(rbs[0])
                    for new_x,new_y,new_z in [(pos_x+x,pos_y+y,pos_z+z)]
                ]
            )
                for t in dict(poss)
                if s not in poss
                for i,neighbors in diffs[t].items()
                if s not in poss
                for j,new_neighbors in new_diffs.items()
                if s not in poss
                if len(neighbors.intersection(new_neighbors)) >= 11
                for loc_x,loc_y,loc_z in [locs[t][i]]
                for new_x,new_y,new_z in [rbs[0][j]]
                for pos_x,pos_y,pos_z in [(loc_x-new_x,loc_y-new_y,loc_z-new_z)]
            ]
        )
        for _ in scanners
        if len(poss) < len(scanners)
        for s,beacons in enumerate(scanners)
        if s not in poss
        for rbs in [[beacons.copy()]]
        for _ in range(4)
        if s not in poss
        for _ in [rbs.append([(y,-x,z) for x,y,z in rbs.pop()])]
        for _ in range(4)
        if s not in poss
        for _ in [rbs.append([(z,y,-x) for x,y,z in rbs.pop()])]
        for _ in range(4)
        if s not in poss
        for _ in [rbs.append([(y,-x,z) for x,y,z in rbs.pop()])]
        for new_diffs in [{}]
    ]]
))
