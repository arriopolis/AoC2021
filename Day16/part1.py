import sys
s = sys.stdin.read().strip()
b = sum((list(map(int,bin(int(c,16))[2:].zfill(4))) for c in s), [])

tot_version = 0
ptr = 0

def parse_packet(b):
    global ptr, tot_version
    version = int(''.join(map(str,b[ptr:ptr+3])),2)
    tot_version += version
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
    return (t,args)

parse_packet(b)
print(tot_version)
