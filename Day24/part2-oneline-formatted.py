print(next(min(''.join(map(str,i)) for s,i in states.items() if s[1] == 0)
    for instrs in [[line.strip().split() for line in open('input.txt')]]
    for new_instrs,to_add in [([],{'w':[],'x':[],'y':[],'z':[]})]
    for _ in [[(
            to_add[instr[1]].append(instr)
        ) if instr[0] == 'inp' else (
            new_instrs.extend(to_add[instr[1]]),
            to_add[instr[1]].clear(),
            (
                new_instrs.extend(to_add[instr[2]]),
                to_add[instr[2]].clear()
            ) if instr[2] in to_add else None,
            new_instrs.append(instr)
        )
        for instr in instrs
    ]]
    for instrs,new_instrs,to_add in [(new_instrs,[],{'w':[],'x':[],'y':[],'z':[]})]
    for _ in [[(
            to_add[instr[1]].append(instr)
        ) if instr[0] == 'mul' and instr[2] == '0' else (
            new_instrs.extend(to_add[instr[1]]),
            to_add[instr[1]].clear(),
            (
                new_instrs.extend(to_add[instr[2]]),
                to_add[instr[2]].clear()
            ) if len(instr) > 2 and instr[2] in to_add else None,
            new_instrs.append(instr)
        )
        for instr in reversed(instrs)
    ]]
    for instrs in [[
        instr
        for instr in list(reversed(new_instrs))
        if not (instr[0] == 'div' and instr[2] == '1')
    ]]
    for b in [[1]]
    for _ in [[
        b.append(b.pop() * int(instr[2]))
        for instr in instrs
        if instr[0] == 'div' and instr[1] == 'z'
    ]]
    for states in [{(0,0,0,0) : tuple()}]
    for _ in [[None
        for k,instr in enumerate(instrs)
        for _ in [print(f"Instruction: {k}/{len(instrs)}: {instr}.", ' '*40, end = '\r')]
        for _ in [
            b.append(b.pop() // int(instr[2]))
            if instr[0] == 'div' and instr[1] == 'z' else None
        ]
        for new_states in [{}]
        for _ in [
            [
                new_states.update({new_state : new_input})
                for j in ['wxyz'.index(instr[1])]
                for s,i in states.items()
                for n in range(9,0,-1)
                for new_input in [tuple(list(i) + [n])]
                for new_state in [tuple(list(s)[:j] + [n] + list(s)[j+1:])]
                if new_state not in new_states or new_states[new_state] >= i
            ] if instr[0] == 'inp' else [
                new_states.update({new_state : i})
                for j in ['wxyz'.index(instr[1])]
                for s,i in states.items()
                for op1 in [s[j]]
                for op2 in [s['wxyz'.index(instr[2])] if instr[2] in 'wxyz' else int(instr[2])]
                for new_state in [
                    tuple(list(s)[:j] + [
                        op1 + op2 if instr[0] == 'add' else
                        op1 * op2 if instr[0] == 'mul' else
                        (abs(op1) // abs(op2)) * (-1 if op1 < 0 else 1) * (-1 if op2 < 0 else 1) if instr[0] == 'div' else
                        op1 % op2 if instr[0] == 'mod' else
                        1 if op1 == op2 else 0
                    ] + list(s)[j+1:])
                ]
                if new_state[3] < b[0]
                if new_state not in new_states or new_states[new_state] >= i
            ]
        ]
        for _ in [(
            states.clear(),
            states.update(new_states)
        )]
    ]]
),' '*40)
