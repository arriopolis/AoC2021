import sys

closing = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

scores = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

all_scores = []
for line in sys.stdin:
    stack = []
    for c in line.strip():
        if c in '([{<':
            stack.append(c)
        else:
            if not stack or closing[stack[-1]] != c: break
            stack.pop()
    else:
        score = 0
        for c in reversed(stack):
            score = score * 5 + scores[closing[c]]
        all_scores.append(score)
all_scores.sort()
print(all_scores[len(all_scores)//2])
