import sys

instrs = []
for line in sys.stdin:
    instrs.append(line.strip().split())

# Push back the inputs as far as possible
new_instrs = []
to_add = {}
for instr in instrs:
    if instr[0] == 'inp':
        if instr[1] not in to_add: to_add[instr[1]] = []
        to_add[instr[1]].append(instr)
    else:
        if instr[1] in to_add and to_add[instr[1]]:
            new_instrs.extend(to_add[instr[1]])
            to_add[instr[1]] = []
        if instr[2] in 'wxyz' and instr[2] in to_add and to_add[instr[2]]:
            new_instrs.extend(to_add[instr[2]])
            to_add[instr[2]] = []
        new_instrs.append(instr)
instrs = new_instrs

# Pull multiplication by 0 as far forward as possible
new_instrs = []
to_add = {}
for instr in reversed(instrs):
    if instr[0] == 'mul' and instr[2] == '0':
        if instr[1] not in to_add: to_add[instr[1]] = []
        to_add[instr[1]].append(instr)
    else:
        if instr[1] in to_add and to_add[instr[1]]:
            new_instrs.extend(to_add[instr[1]])
            to_add[instr[1]] = []
        if len(instr) > 2 and instr[2] in 'wxyz' and instr[2] in to_add and to_add[instr[2]]:
            new_instrs.extend(to_add[instr[2]])
            to_add[instr[2]] = []
        new_instrs.append(instr)
instrs = list(reversed(new_instrs))

# Remove divisions by one
instrs = [instr for instr in instrs if not (instr[0] == 'div' and instr[2] == '1')]

# Maximum bound on z
b = 1
for instr in instrs:
    if instr[0] == 'div' and instr[1] == 'z':
        b *= int(instr[2])

states = {(0,0,0,0) : tuple()}
for k,instr in enumerate(instrs):
    print(f"Instruction: {k}/{len(instrs)}: {instr}.")

    if instr[0] == 'div' and instr[1] == 'z':
        b //= int(instr[2])
        print("New bound for z:", b)

    new_states = {}
    if instr[0] == 'inp':
        j = 'wxyz'.index(instr[1])
        for s,i in states.items():
            for n in range(1,10):
                new_input = tuple(list(i) + [n])
                new_state = list(s)
                new_state[j] = n
                new_state = tuple(new_state)
                if new_state in new_states and new_states[new_state] > i: continue
                new_states[new_state] = new_input
    elif instr[0] in ['add', 'mul', 'div', 'mod', 'eql']:
        j = 'wxyz'.index(instr[1])
        for s,i in states.items():
            op1 = s[j]
            op2 = s['wxyz'.index(instr[2])] if instr[2] in 'wxyz' else int(instr[2])
            new_state = list(s)
            if instr[0] == 'add':
                new_state[j] = op1 + op2
            elif instr[0] == 'mul':
                new_state[j] = op1 * op2
            elif instr[0] == 'div':
                new_state[j] = abs(op1) // abs(op2)
                if op1 < 0: new_state[j] *= -1
                if op2 < 0: new_state[j] *= -1
            elif instr[0] == 'mod':
                new_state[j] = op1 % op2
            elif instr[0] == 'eql':
                new_state[j] = 1 if op1 == op2 else 0
            else: raise ValueError("This instruction is not understood.")
            new_state = tuple(new_state)

            # Prune if z becomes too large
            if new_state[3] >= b: continue

            if new_state in new_states and new_states[new_state] > i: continue
            new_states[new_state] = i
    states = new_states
    print("Number of states:", len(states))

print(max(''.join(map(str,i)) for s,i in states.items() if s[1] == 0))
