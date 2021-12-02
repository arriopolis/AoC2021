import sys

instrs = []
for line in sys.stdin:
    instr, n = line.strip().split()
    instrs.append((instr, int(n)))

hor = 0
depth = 0
aim = 0
for instr, n in instrs:
    if instr == 'forward':
        hor += n
        depth += n*aim
    elif instr == 'up':
        aim -= n
    elif instr == 'down':
        aim += n

print(hor * depth)
