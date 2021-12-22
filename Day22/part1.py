import sys
import itertools as it

instrs = []
for line in sys.stdin:
    b,coords = line.strip().split()
    b = True if b == 'on' else False
    (xmin,xmax),(ymin,ymax),(zmin,zmax) = [[int(y) for y in x[2:].split('..')] for x in coords.split(',')]
    instrs.append((b,((xmin,xmax+1),(ymin,ymax+1),(zmin,zmax+1))))

def intersect(cube1, cube2):
    (xmin1,xmax1),(ymin1,ymax1),(zmin1,zmax1) = cube1
    (xmin2,xmax2),(ymin2,ymax2),(zmin2,zmax2) = cube2

    # Look for a separating plane
    if xmin1 >= xmax2 or xmin2 >= xmax1:
        return set(),set([cube1]),set([cube2])
    if ymin1 >= ymax2 or ymin2 >= ymax1:
        return set(),set([cube1]),set([cube2])
    if zmin1 >= zmax2 or zmin2 >= zmax1:
        return set(),set([cube1]),set([cube2])

    # Split
    all_xs = sorted(set([xmin1,xmax1,xmin2,xmax2]))
    all_ys = sorted(set([ymin1,ymax1,ymin2,ymax2]))
    all_zs = sorted(set([zmin1,zmax1,zmin2,zmax2]))

    xs1 = all_xs[all_xs.index(xmin1):all_xs.index(xmax1)+1]
    xs2 = all_xs[all_xs.index(xmin2):all_xs.index(xmax2)+1]
    ys1 = all_ys[all_ys.index(ymin1):all_ys.index(ymax1)+1]
    ys2 = all_ys[all_ys.index(ymin2):all_ys.index(ymax2)+1]
    zs1 = all_zs[all_zs.index(zmin1):all_zs.index(zmax1)+1]
    zs2 = all_zs[all_zs.index(zmin2):all_zs.index(zmax2)+1]

    # Loop over subcubes of cube 1
    cubelets1 = set(it.product(zip(xs1[:-1],xs1[1:]), zip(ys1[:-1],ys1[1:]), zip(zs1[:-1],zs1[1:])))
    cubelets2 = set(it.product(zip(xs2[:-1],xs2[1:]), zip(ys2[:-1],ys2[1:]), zip(zs2[:-1],zs2[1:])))

    # Return the cubelets
    return cubelets1.intersection(cubelets2), cubelets1.difference(cubelets2), cubelets2.difference(cubelets1)

def size(cube):
    (xmin,xmax),(ymin,ymax),(zmin,zmax) = cube
    return (xmax - xmin) * (ymax - ymin) * (zmax - zmin)

cubelets = set()
for b,cube1 in instrs:
    (xmin,xmax),(ymin,ymax),(zmin,zmax) = cube1
    if max(abs(xmin),abs(xmax),abs(ymin),abs(ymax),abs(zmin),abs(zmax)) > 51: continue

    new_cubelets = set([cube1] if b else [])
    for cube2 in cubelets:
        i,c1,c2 = intersect(cube1,cube2)
        new_cubelets.update(c2)
    cubelets = new_cubelets

print(sum(size(cube) for cube in cubelets))
