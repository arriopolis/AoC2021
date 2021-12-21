import sys

poss = [int(line.strip()[28:]) for line in sys.stdin]
scores = [0,0]

ctr = 0
turn = 1
while all(s < 1000 for s in scores):
    ctr += 3
    turn = 1-turn

    poss[turn] = (poss[turn] + 3 * ctr - 4) % 10 + 1
    scores[turn] += poss[turn]

print(scores[1-turn] * ctr)
