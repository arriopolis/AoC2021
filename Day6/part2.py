import sys

ds = {}
for n in sys.stdin.read().strip().split(','):
    if int(n) not in ds: ds[int(n)] = 0
    ds[int(n)] += 1

for _ in range(256):
    new_ds = {}
    for n,k in ds.items():
        if n == 0:
            if 6 not in new_ds: new_ds[6] = 0
            new_ds[6] += k
            if 8 not in new_ds: new_ds[8] = 0
            new_ds[8] += k
        else:
            if n-1 not in new_ds: new_ds[n-1] = 0
            new_ds[n-1] += k
    ds = new_ds
print(sum(new_ds.values()))
