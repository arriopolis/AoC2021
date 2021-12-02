import sys

instrs = []
for line in sys.stdin:
    instr, n = line.strip().split()
    instrs.append((instr, int(n)))

hor = 0
depth = 0
for instr, n in instrs:
    if instr == 'forward':
        hor += n
    elif instr == 'up':
        depth -= n
    elif instr == 'down':
        depth += n

print(hor * depth)
