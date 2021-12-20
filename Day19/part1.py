import sys

scanners = []
for line in sys.stdin:
    if not line.strip(): continue
    if line[:3] == '---':
        beacons = []
        scanners.append(beacons)
    else:
        x,y,z = map(int,line.strip().split(','))
        beacons.append((x,y,z))

grid = set(scanners[0])
poss = {0 : (0,0,0)}
locs = {0 : {}}
diffs = {0 : {}}
for i,(x,y,z) in enumerate(scanners[0]):
    locs[0][i] = (x,y,z)
for i,(x1,y1,z1) in enumerate(scanners[0]):
    diffs[0][i] = set()
    for j,(x2,y2,z2) in enumerate(scanners[0]):
        if i == j: continue
        diff = x2-x1,y2-y1,z2-z1
        diffs[0][i].add(diff)

while len(poss) < len(scanners):
    for s,beacons in enumerate(scanners):
        if s in poss: continue

        rotated_beacons = beacons
        for _ in range(4):
            # Perform a Z rotation
            rotated_beacons = [(y,-x,z) for x,y,z in rotated_beacons]

            for _ in range(4):
                # Perform a Y rotation
                rotated_beacons = [(z,y,-x) for x,y,z in rotated_beacons]

                for _ in range(4):
                    # Perform a Z rotation
                    rotated_beacons = [(y,-x,z) for x,y,z in rotated_beacons]

                    # Calculate the differences
                    new_diffs = {}
                    for i,(x1,y1,z1) in enumerate(rotated_beacons):
                        new_diffs[i] = set()
                        for j,(x2,y2,z2) in enumerate(rotated_beacons):
                            if i == j: continue
                            diff = x2-x1,y2-y1,z2-z1
                            new_diffs[i].add(diff)

                    for t in poss:
                        for i,neighbors in diffs[t].items():
                            for j,new_neighbors in new_diffs.items():
                                if len(neighbors.intersection(new_neighbors)) >= 11:
                                    print(f"Found overlap between scanners {t} and {s}.")
                                    loc_x,loc_y,loc_z = locs[t][i]
                                    new_x,new_y,new_z = rotated_beacons[j]
                                    pos_x,pos_y,pos_z = loc_x-new_x,loc_y-new_y,loc_z-new_z
                                    print(f"Location of scanner {s}: {pos_x}, {pos_y}, {pos_z}")

                                    poss[s] = (pos_x,pos_y,pos_z)
                                    diffs[s] = new_diffs
                                    locs[s] = {}
                                    for i,(x,y,z) in enumerate(rotated_beacons):
                                        new_x,new_y,new_z = pos_x+x,pos_y+y,pos_z+z
                                        locs[s][i] = (new_x,new_y,new_z)
                                        grid.add((new_x,new_y,new_z))
                                    break
                            else: continue
                            break
                        else: continue
                        break
                    else: continue
                    break
                else: continue
                break
            else: continue
            break
print(len(grid))
