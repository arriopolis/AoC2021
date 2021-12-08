import sys

count = 0
for line in sys.stdin:
    a,b = line.strip().split(' | ')
    for x in b.split():
        if len(x) in [2,3,4,7]:
            count += 1
print(count)
