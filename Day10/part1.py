import sys

closing = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

scores = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

score = 0
for line in sys.stdin:
    stack = []
    for c in line.strip():
        if c in '([{<':
            stack.append(c)
        else:
            if not stack or closing[stack[-1]] != c: break
            stack.pop()
    else: continue
    score += scores[c]
print(score)
