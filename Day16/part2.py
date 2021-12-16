from functools import reduce
import sys
s = sys.stdin.read().strip()
b = sum((list(map(int,bin(int(c,16))[2:].zfill(4))) for c in s), [])

ptr = 0

def parse_packet(b):
    global ptr
    version = int(''.join(map(str,b[ptr:ptr+3])),2)
    t = int(''.join(map(str,b[ptr+3:ptr+6])),2)

    # Literal type
    if t == 4:
        ptr += 6
        n = []
        while True:
            n += b[ptr+1:ptr+5]
            ptr += 5
            if b[ptr-5] == 0: break
        n = int(''.join(map(str,n)),2)
        return n

    # Parse arguments of operator
    lt = b[ptr+6]
    if lt == 0:
        l = int(''.join(map(str,b[ptr+7:ptr+22])),2)
        ptr += 22
        start_ptr = ptr
        args = []
        while ptr < start_ptr + l:
            args.append(parse_packet(b))

    # lt == 1
    else:
        n = int(''.join(map(str,b[ptr+7:ptr+18])),2)
        ptr += 18
        args = []
        for _ in range(n):
            args.append(parse_packet(b))

    # Return the result
    if t == 0: return sum(args)
    if t == 1: return reduce(lambda x,y : x*y, args, 1)
    if t == 2: return min(args)
    if t == 3: return max(args)
    if t == 5: return int(args[0] > args[1])
    if t == 6: return int(args[0] < args[1])
    if t == 7: return int(args[0] == args[1])
    raise ValueError(f"Type ID {f} not understood.")

print(parse_packet(b))
